from django.http import HttpResponse, request


def simple_route(request):
    status = 200
    print(request)
    return HttpResponse(status=status)
