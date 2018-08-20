from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..models import Review
from ..forms import ReviewForm

def home(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/home.html', {'reviews': reviews})
    
@login_required
def add(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('/reviews/#' + str(review.pk))
    else:
        form = ReviewForm()        
    return render(request, 'reviews/edit.html', {'form': form})

@login_required
def edit(request, pk):
    try:
        reviews = Review.objects.filter(pk=pk)
    except ValueError:
        reviews = False
    if not reviews:
        return render(request, 'manager/error.html', {'msg': "The review you're looking for doesn't exist"})

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=reviews[0])
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('/reviews/#' + str(review.pk))
    else:
        form = ReviewForm(instance=reviews[0])
        
    return render(request, 'reviews/edit.html', {'form': form})

@login_required
def delete(request, pk):
    reviews = Review.objects.filter(pk=pk)
    if not reviews:
        return render(request, 'manager/error.html', {'msg': "The review you're looking for doesn't exist"})

    reviews[0].delete()
    return redirect('/reviews/')
