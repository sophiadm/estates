from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models import BlogPost
from ..forms import BlogForm

def home(request):
    posts = BlogPost.objects.all().order_by('-created_date')
    return render(request, 'blog/home.html', {'posts': [posts[i:i + 5] for i in range(0, len(posts), 5)]})
    
def see(request, url):
    title = url.replace('_', ' ')
    posts = BlogPost.objects.filter(title=title)
    if not posts:
        return render(request, 'manager/error.html', {'msg': "The blog post you're looking for doesn't exist"})

    return render(request, 'blog/view.html', {'post': posts[0]})

@login_required
def add(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            title = form.cleaned_data['title']
            if '_' in title:
                return render(request, 'blog/edit.html', {'form': form, 'msg':"Sorry, but you can't use underscores in the title"})

            if BlogPost.objects.filter(title=title):
                return render(request, 'blog/edit.html', {'form': form, 'msg':'A post with that title already exists <a href="/blog/'+blog.url()+'">here</a>'})

            blog.save()
            return redirect('/blog/' + blog.url())
    else:
        form = BlogForm()
        
    return render(request, 'blog/edit.html', {'form': form})

@login_required
def edit(request, url):
    title = url.replace('_', ' ')
    posts = BlogPost.objects.filter(title=title)
    if not posts:
        return render(request, 'manager/error.html', {'msg': "The blog post you're looking for doesn't exist"})

    if request.method == "POST":
        form = BlogForm(request.POST, instance=posts[0])
        if form.is_valid():
            blog = form.save(commit=False)
            newtitle = form.cleaned_data['title']
            
            if '_' in title:
                return render(request, 'blog/edit.html', {'form': form, 'msg':"Sorry, but you can't use underscores in the title"})

            if title != newtitle and BlogPost.objects.filter(title=newtitle):
                return render(request, 'blog/edit.html', {'form': form, 'msg':'A post with that title already exists <a href="/blog/'+blog.url()+'">here</a>'})

            blog.save()
            return redirect('/blog/' + blog.url())
    else:
        form = BlogForm(instance=posts[0])
        
    return render(request, 'blog/edit.html', {'form': form})

@login_required
def delete(request, url):
    title = url.replace('_', ' ')
    posts = BlogPost.objects.filter(title=title)
    if not posts:
        return render(request, 'manager/error.html', {'msg': "The blog post you're looking for doesn't exist"})

    posts[0].delete()
    return redirect('/blog/')
