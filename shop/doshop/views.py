from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request) :
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    context = {
        'products' : products ,
        'categories' : categories
    }
    return render(request,'doshop/home.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    categories = Category.objects.all()
    context = {
        'product' : product ,
        'categories' : categories
    }
    return render(request,'doshop/product_detail.html',context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    context = {
        'category' : category ,
        'categories' : categories
    }
    return render(request,'doshop/category_detail.html',context)