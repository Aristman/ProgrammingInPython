from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Blog, Entry, Author


def index(request):
    response = HttpResponse('Блог создан')
    blog = Blog.objects.all()
    if blog.count == 0:
        create_blog()
    context =dict()
    context['blog'] = blog
    return render(request, 'index.html', context=context)

def create_blog():
    blog = Blog(name='Мой первый блог', tagline='С этого момента можно считать, что я начинаю писать свой сайт')
    blog.save()
    print(blog.objects.all())