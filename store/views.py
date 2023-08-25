from django.contrib import messages
from django.core.paginator import PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.utils.translation import gettext
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, TemplateView


def index(request):
    return HttpResponse(
        "Hello there, globomantics e-commerce store front coming here..."
    )


def detail(request):
    return HttpResponse("Hello there, globomantics e-commerce store front detail pages coming here...")


def logout(request):
    try:
        del request.session['customer']
    except KeyError:
        print("Error while logging out.")

    return HttpResponse("You're logged out.")


@csrf_exempt
@cache_page(900)
@require_http_methods(["GET"])
def electronics(request):
    items = ("Windows PC", "Apple Mac", "Apple iPhone", "Lenovo", "Samsung",
             "Google")

    if request.method == 'GET':
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        name = "John Doe"
        message = gettext("Customer Successfully Fetched.")
        messages.info(request, message)

        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)

        if not request.session.has_key('customer'):
            request.session['customer'] = name
            print("Setting session.")

        response = render(request, 'store/list.html', {'items': items})

        if request.COOKIES.get('visits'):
            value = int(request.COOKIES.get('visits'))
            print("Getting cookie.")
            response.set_cookie('visits', value + 1)
        else:
            value = 1
            print("Setting cookie.")
            response.set_cookie('visits', value)

        return response
    elif request.method == 'POST':
        return HttpResponseNotFound("POST method is not allowed, dude")


class ElectronicsView(View):
    def get(self, request):
        items = ("Android", "Slimbook", "Apple iPad", "Dell", "Motorola",
                 "Toshiba")

        if request.method == 'GET':
            paginator = Paginator(items, 2)
            pages = request.GET.get('page', 1)
            self.process()

            try:
                items = paginator.page(pages)
            except PageNotAnInteger:
                items = paginator.page(1)
            return render(request, 'store/list.html', {'items': items})
        elif request.method == 'POST':
            return HttpResponseNotFound("POST method is not allowed, dude")

    def process(self):
        print("\n*** We are processing Electronics ***\n")


class ComputersView(ElectronicsView):
    def process(self):
        print("\n--- We are processing Computers ---\n")


class MobileView:
    def process(self):
        print("\n### We are processing Mobile phones ###\n")


class EquipmentView(MobileView, ComputersView):
    pass


class ElectronicsTemplateView(TemplateView):
    template_name = 'store/list.html'

    def get_context_data(self, **kwargs):
        items = ("Verbatim", "Maxtor", "Kindle", "Sandisk", "Raspberry Pi",
                 "Remarkable")
        context = {'items': items}
        return context


class ElectronicsListView(ListView):
    template_name = 'store/list2.html'

    queryset = ("LG", "Garmin", "Suntoo", "Belkin", "Arduino", "Apple Pencil")
    context_object_name = 'items'
    paginate_by = 2
