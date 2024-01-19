from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(response):
    return HttpResponse("Rango says here is the about page. <br> <a href='/rango/'>Index</a>")

# Create your views here.
