from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    return HttpResponse('OK')

def my_view(request):
    t = loader.get_template('templates/core.html')
    context = {'Ключ': 'Первый'}
    return HttpResponse(t.render(context, request))
