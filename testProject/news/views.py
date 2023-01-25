from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

def index(request):
    posts = News.objects.order_by('-date')
    return render(request, 'news/index.html', {'posts': posts, 'title': "Main page"})

def second(request):
    posts = News.objects.all()
    return render(request, 'news/second.html', {'posts': posts, 'title': "Second page"})


def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
