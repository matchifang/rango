from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    html = "<html><h1>This is the main page</h1><a href='/rango/about/'>About</a></html>"
    return HttpResponse(html)


def about(request):
    html = "<html><h1>This is the about page</h1><a href='/rango/'>Main page</a></html>"
    return HttpResponse(html)