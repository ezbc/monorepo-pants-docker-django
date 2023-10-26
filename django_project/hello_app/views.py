from django.http import HttpResponse
from library.greet import return_greeting


def index(request):
    return HttpResponse("Hello from the hello_app/views.py file 🔥!")


def greet(request):
    return HttpResponse(return_greeting())
