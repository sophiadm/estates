from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import BlogPost, Property
from django.core.mail import send_mail
from ..forms import EmailForm
def home(request):
    blogposts = BlogPost.objects.all()
    if blogposts:
        blogpost = blogposts.order_by('-created_date')[0]
        description = blogpost.info(300)
    else:
        blogpost = "no blogs"
    props = Property.objects.all().filter(available=True)
    if props:
        prop = props[0]
    else:
        prop = "no props"

    return render(request, 'manager/home.html', {'blog': blogpost,
                                                 'bloginfo':description,
                                                 'property':prop})

def about(request):
    return render(request, 'manager/about.html')

def contact(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        
        if form.is_valid():
            mail = form.cleaned_data
            
            send_mail(
                'Automated Eastgate Estates Website Enquiry',
                mail['msg'],
                mail['email'],
                [''],
                fail_silently = False,
            )
            
            return render(request, 'manager/error.html', {'msg': "Thanks, we will be in touch as soon as possible"})

    else:
        form = EmailForm()

    return render(request, 'manager/contact.html', {'form': form})    

def no_match(request):
    return render(request, 'manager/error.html', {'msg': "The page you're looking for doesn't exist",})
