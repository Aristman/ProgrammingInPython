from django.db.models import Count
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.template import loader

from core.models import Topic, Category


def index(request):
    topics = Topic.objects.all().annotate(Count('category'))
    categories = Category.objects.all()
    q = request.GET.get('q')
    if q is not None:
        topics = topics.filter(title__icontains=q)
    category_pk = request.GET.get('category')
    if category_pk is not None:
        topics = topics.filter(category__pk=category_pk)
    return render(request, 'core/index.html', context={
        'topics': topics,
        'categories': categories
    })

def topic_details(request, pk):
    try:
        topic = Topic.objects.get(pk=pk)
    except:
        raise Http404
    return render(request, 'core/topic_details.html', context={
        'topic': topic,
    })

def category_details(request, pk):
    return render(request, 'core/category_details.html')

def my_view(request):
    t = loader.get_template('templates/core.html')
    context = {'Ключ': 'Первый'}
    return HttpResponse(t.render(context, request))
