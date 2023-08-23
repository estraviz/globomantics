from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page


def index(request):
    return HttpResponse("Hello there, globomantics e-commerce store front coming here...")


def detail(request):
    return HttpResponse("Hello there, globomantics e-commerce store front detail pages coming here...")


@csrf_exempt
@cache_page(900)
@require_http_methods(["GET"])
def electronics(request):
    if request.method == 'GET':
        print(request.headers)
        print("---------\n", request)
        return HttpResponse("Hello there, globomantics e-commerce store front Electronics pages coming here...")
    elif request.method == 'POST':
        return HttpResponseNotFound("POST method is not allowed, dude")
