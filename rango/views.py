from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(response):
    context_dict = {'boldmessage': 'This tutorial has been put together by Sam.'}
    return render(response, 'rango/about.html', context=context_dict)
    
# Create your views here.
