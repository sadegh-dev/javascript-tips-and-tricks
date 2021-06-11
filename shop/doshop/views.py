from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request) :
    products = Product.objects.filter(available=True)
    context = {
        'products' : products ,
    }
    return render(request,'doshop/home.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product' : product ,
    }
    return render(request,'doshop/product_detail.html',context)