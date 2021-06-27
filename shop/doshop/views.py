from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Product, Company
from cart.forms import CartAddForm
from .forms import InsertProductForm

def home(request) :
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    companies = Company.objects.all()
    context = {
        'products' : products ,
        'categories' : categories,
        'companies' : companies ,
    }
    return render(request,'doshop/home.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    categories = Category.objects.all()
    companies = Company.objects.all()
    form = CartAddForm()

    context = {
        'product' : product ,
        'categories' : categories ,
        'companies' : companies,
        'form' : form
    }
    return render(request,'doshop/product_detail.html',context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    companies = Company.objects.all()
    context = {
        'category' : category ,
        'categories' : categories ,
        'companies' : companies
    }
    return render(request,'doshop/category_detail.html',context)


def company_detail(request, slug):
    company = get_object_or_404(Company, slug=slug)
    categories = Category.objects.all()
    companies = Company.objects.all()
    context = {
        'company' : company ,
        'companies' : companies ,
        'categories' : categories
    }
    return render(request,'doshop/company_detail.html',context)


def all_specialـprice(request) :
    products = Product.objects.filter(available=True, specialـprice__isnull=False)
    categories = Category.objects.all()
    companies = Company.objects.all()
    context = {
        'products' : products ,
        'categories' : categories,
        'companies' : companies ,
    }
    return render(request,'doshop/specialـprice.html', context)


def page_not_found(request):
    categories = Category.objects.all()
    companies = Company.objects.all()
    context = {
        'categories' : categories,
        'companies' : companies ,
    }
    return render(request,'doshop/404.html', context)



# ---- Manager --------- # 
@login_required
def insert_product(request):
    if request.user.access_level == 'o' :
        if request.method=='POST':
            form = InsertProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'ثبت کالای جدید با موفقیت انجام شد','success')
                return redirect('doshop:home')
        else :
            form = InsertProductForm()
        context = {
            'form' : form
        }
        return render(request,'accounts/manager/insert_product.html',context)
    else :
        return redirect('doshop:home')



@login_required
def edit_product(request, slug):
    if request.user.access_level == 'o' :
        the_product = get_object_or_404(Product, slug=slug)
        if request.method=='POST':
            form = InsertProductForm(request.POST, request.FILES, instance=the_product)
            if form.is_valid():
                slug = form.cleaned_data['slug']
                form.save()
                messages.success(request,'ویرایش مشخصات کالا با موفقیت انجام شد','success')
                return redirect('doshop:product-detail', slug )
        else :
            form = InsertProductForm(instance=the_product)
        context = {
            'form' : form ,
        }
        return render(request,'accounts/manager/edit_product.html',context)
    else :
        return redirect('doshop:home')









# ---- EndManager ------ #