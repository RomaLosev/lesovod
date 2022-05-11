from django.shortcuts import render
from posts.models import Post


def index(request):
    template = 'index.html'
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, template, context)


def about(request):
    template = 'about.html'
    title = 'О компании'
    context = {
        'title': title,
    }
    return render(request, template, context)


def employers(request):
    template = 'employers.html'
    title = 'Сотрудники'
    context = {
        'title': title,
    }
    return render(request, template, context)


def posts(request):
    template = 'posts.html'
    title = 'Блог'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)
