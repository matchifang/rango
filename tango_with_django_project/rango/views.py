
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    html = "<html><h1>This is the main page</h1><a href='/rango/about/'>About</a></html>"
    return HttpResponse(html)


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier. # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    html = "<html><h1>This is the about page</h1><a href='/rango/'>Main page</a></html>"
    return HttpResponse(html)