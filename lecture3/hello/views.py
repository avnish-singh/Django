from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html") # render() function takes the request object, the template name and an optional context dictionary and returns an HttpResponse object with the rendered template.

def brian(request):
    return HttpResponse("Hello, Brian")

def avnish(request):
    return HttpResponse("Hello, Avnish")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize() # capitalize() function capitalizes the first letter of the name and makes the rest lowercase.
    })