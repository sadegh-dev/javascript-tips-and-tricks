from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from accounts.models import User
from doshop.models import Category, Company, Product
from orders.models import Order

from .forms import UserApiForm

from .serializers import CategorySerializer, CompanySerializer, specialPriceProductsSerializer, ProductsOFCategorySerializer



@api_view()
def test_connect(request):
    data = {
        "connect" : "True" ,
    }
    return Response(data)


@api_view(['GET','POST'])
def test_post_get(request):
    if request.method == 'POST':
        data = {
            "connect" : "is POST" ,
        }
    else :
        data = {
            "coonect" : "is GET" ,
        }
    return Response(data)


@api_view()
def categories(requests):
    categories = Category.objects.all()
    ser_data = CategorySerializer(categories, many=True)
    return Response(ser_data.data)


@api_view()
def companies(request):
    companies = Company.objects.all()
    ser_data = CompanySerializer(companies, many=True)
    return Response(ser_data.data)


@api_view()
def special_price_products(request):
    products = Product.objects.filter(available=True)
    ser_data = specialPriceProductsSerializer(products, many=True)
    return Response(ser_data.data)


@api_view()
def category_products(request, slug):
    products = Product.objects.filter(available=True, category__slug=slug)
    ser_data = ProductsOFCategorySerializer(products, many=True)
    return Response(ser_data.data)


@login_required
def get_token(request):
    form = UserApiForm()
    context = {
        'form' : form,
    }
    return render(request,'doapi/get_token.html',context)

