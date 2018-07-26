from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..models import QandA
from ..forms import QandAForm

def home(request):
    faqs = QandA.objects.all()
    return render(request, 'qandas/home.html', {'faqs': faqs})
    
@login_required
def add(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            
            if QandA.objects.filter(title=title):
                return render(request, 'qandas/edit.html',
                              {'form': form,
                               'msg':'That question has already benn asked <a href="/faqs#'+str(faq.pk)+'">here</a>'})

            faq.save()
            return redirect('/faqs/#' + str(faq.pk))
    else:
        form = QandAForm()        
    return render(request, 'qandas/edit.html', {'form': form})

@login_required
def edit(request, pk):
    faqs = QandA.objects.filter(pk=pk)
    if not faqs:
        return render(request, 'manager/error.html', {'msg': "The faq you're looking for doesn't exist"})

    if request.method == "POST":
        form = QandAForm(request.POST, instance=faqs[0])
        if form.is_valid():
            faq = form.save(commit=False)

            if faqs[0].question != newtitle and BlogPost.objects.filter(title=newtitle):
                return render(request, 'qandas/edit.html',
                              {'form': form,
                               'msg':'That question has already benn asked <a href="/faqs#'+str(faq.pk)+'">here</a>'})
            
            faq.save()
            return redirect('/faqs/#' + str(faq.pk))
    else:
        form = ReviewForm(instance=faqs[0])
        
    return render(request, 'qandas/edit.html', {'form': form})

@login_required
def delete(request, pk):
    faqs = QandA.objects.filter(pk=pk)
    if not faqs:
        return render(request, 'manager/error.html', {'msg': "The review you're looking for doesn't exist"})

    faqs[0].delete()
    return redirect('/faqs/')
