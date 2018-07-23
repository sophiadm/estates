
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models import Property
#from ..forms import PropertyForm

def home(request):
    posts = Property.objects.filter(available=True)
    return render(request, 'property/home.html', {'posts': posts})
    
def see(request, url):
    posts = BlogPost.objects.filter(pk=pk)
    if not posts:
        return render(request, 'manager/error.html', {'msg': "The blog post you're looking for doesn't exist"})

    if posts[0].available = False:
        return render(request, 'manager/error.html', {'msg': "Unfortunately, the property you are looking for is no longer available to rent"})
        
    return render(request, 'property/view.html', {'property': posts[0]})

@login_required
def add(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            prop = form.save(commit=False)
            prop.save()
            return redirect('/properties/' + prop.pk)
    else:
        form = BlogForm()        
        return render(request, 'properties/edit.html', {'form': form})

@login_required
def edit(request, pk):
    posts = Property.objects.filter(pk=pk)
    if not posts:
        return render(request, 'manager/error.html', {'msg': "The property you're looking for doesn't exist"})

    if request.method == "POST":
        form = PropertyForm(request.POST, instance=posts[0])
        if form.is_valid():
            prop = form.save(commit=False)
            prop.save()
            return redirect('/properties/' + prop.pk)
    else:
        form = PropertyForm(instance=posts[0])
        
    return render(request, 'properties/edit.html', {'form': form})

@login_required
def delete(request, url):
    title = url.replace('_', ' ')
    posts = BlogPost.objects.filter(title=title)
    if not posts:
        return render(request, 'manager/error.html', {'msg': "The blog post you're looking for doesn't exist"})

    posts[0].delete()
    return redirect('/blog/')
