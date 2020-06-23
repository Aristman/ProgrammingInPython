from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST


def simple_route(request):
    status = 200 if request.method == 'GET' else 405
    return HttpResponse('', status=status)


def slug_route(request, slug):
    return HttpResponse(slug)


def sum_route(request, a, b):
    return HttpResponse(str(int(a) + int(b)))


def get_sum(params):
    response = HttpResponse()
    response.status_code = 400
    sum = 0
    try:
        for it in params:
            sum += int(params[it])
        response.status_code = 200 if len(params) == 2 else 400
        response.content = str(sum)
    except Exception:
        return response
    return response


@require_GET
def sum_get_method(request):
    return get_sum(request.GET)


@require_POST
def sum_post_method(request):
    return get_sum(request.POST)

