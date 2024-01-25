from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    return render(request, 'rango/index.html', context=context_dict)

def about(response):
    context_dict = {'boldmessage': 'This tutorial has been put together by Sam.'}
    return render(response, 'rango/about.html', context=context_dict)