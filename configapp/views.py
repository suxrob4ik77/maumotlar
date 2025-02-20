from django.shortcuts import render
from unicodedata import category

from .models import *


def index(request):
    news = News.objects.all()
    category = Categories.objects.all()
    context = {
        'news': news,
        "title": "News",
        "category":category,

    }
    return render(request, 'model/index.html', context=context)