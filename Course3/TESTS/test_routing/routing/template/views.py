from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def echo(request):
    context = {}
    if request.method == 'GET':
        context = {'method': 'get'}
        context.update({'params': dict(request.GET)})
    elif request.method == 'POST':
        context = {'method': 'post'}
        context.update({'params': dict(request.POST)})
    context.update({'statement': request.META.get('HTTP_X_PRINT_STATEMENT', 'empty')})
    return render(request, 'echo.html', status=200, context=context)


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
