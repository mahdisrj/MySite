from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index_view(request):
    return render(request, 'website/index.html')


def products_view(request):
    return render(request,'website/products.html')


def contact_view(request):
    return HttpResponse('<h1>contact page<h1>')
