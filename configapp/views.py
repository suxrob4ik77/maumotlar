from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewsForm, UserLoginForm
from .models import *


def index(request):
    news = News.objects.all()
    category = Category.objects.all()
    context = {
        'news': news,
        "title": "News",
        "category":category,

    }
    return render(request, 'model/index.html', context=context)

def add_news(request):
    if request.method=='POST':
        form=NewsForm(request.POST)
        if form.is_valid():
            news=News.objects.create(**form.cleaned_data)
            return redirect('Home')

    else:
        form=NewsForm()
    return render(request,'model/add-news.html',{'form':form})

def add_category(request):
    if request.method=='POST':
        form=NewsForm(request.POST)
        if form.is_valid():
            news=form.save()
            # news=News.objects.create(**form.cleaned_data)
            return redirect(news)

    else:
        form=NewsForm()
    return render(request,'model/add_cat.html',{'form':form})


def about_news(request,new_id):
    new=get_object_or_404(News,id=new_id)
    context={
        "new":new
    }
    return render(request,'model/about_new.html',context)


def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Home')
    else:
        form=UserLoginForm()
    return render(request,'model/login.html',{'form': form})
