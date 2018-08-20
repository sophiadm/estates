
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..models import Property
from ..forms import PropertyForm

def home(request):
    if request.user.is_authenticated:
        posts = Property.objects.all()
    else:
        posts = Property.objects.filter(available=True)
    return render(request, 'properties/home.html', {'posts': posts})
    
def see(request, pk):
    try:
        posts = Property.objects.filter(pk=pk)
    except ValueError:
        posts = False
    if not posts:
        return render(request, 'manager/error.html', {'msg': "The property you're looking for doesn't exist"})

    if posts[0].available == False and not request.user.is_authenticated:
        return render(request, 'manager/error.html', {'msg': "Unfortunately, the property you are looking for is no longer available to rent"})
        
    return render(request, 'properties/view.html', {'property': posts[0]})

@login_required
def add(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            prop = form.save(commit=False)
            prop.save()
            return redirect('/properties/' + str(prop.pk))
    else:
        form = PropertyForm()        
    return render(request, 'properties/edit.html', {'form': form})

@login_required
def edit(request, pk):
    posts = Property.objects.filter(pk=pk)
    if not posts:
        return render(request, 'manager/error.html', {'msg': "The property you're looking for doesn't exist"})

    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES, instance=posts[0])
        if form.is_valid():
            prop = form.save(commit=False)
            prop.save()
            return redirect('/properties/' + str(prop.pk))
    else:
        form = PropertyForm(instance=posts[0])
        
    return render(request, 'properties/edit.html', {'form': form})

@login_required
def delete(request, pk):
    posts = Property.objects.filter(pk=pk)
    if not posts:
        return render(request, 'manager/error.html', {'msg': "The property you're looking for doesn't exist"})

    posts[0].delete()
    return redirect('/properties/')
