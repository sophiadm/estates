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
        form = QandAForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)

            qexists = QandA.objects.filter(question=form.cleaned_data["question"])
            if qexists:
                return render(request, 'qandas/edit.html',
                              {'form': form,
                               'msg':'That question has already benn asked <a href="/faqs#'+str(qexists.pk)+'">here</a>'})

            faq.save()
            return redirect('/faqs/#' + str(faq.pk))
    else:
        form = QandAForm()        
    return render(request, 'qandas/edit.html', {'form': form})

@login_required
def edit(request, pk):
    try:
        faqs = QandA.objects.filter(pk=pk)
    except ValueError:
        faqs = False
    if not faqs:
        return render(request, 'manager/error.html', {'msg': "The faq you're looking for doesn't exist"})

    if request.method == "POST":
        form = QandAForm(request.POST, instance=faqs[0])
        if form.is_valid():
            faq = form.save(commit=False)
            
            faq.save()
            return redirect('/faqs/#' + str(faq.pk))
    else:
        form = QandAForm(instance=faqs[0])
        
    return render(request, 'qandas/edit.html', {'form': form})

@login_required
def delete(request, pk):
    faqs = QandA.objects.filter(pk=pk)
    if not faqs:
        return render(request, 'manager/error.html', {'msg': "The review you're looking for doesn't exist"})

    faqs[0].delete()
    return redirect('/faqs/')
