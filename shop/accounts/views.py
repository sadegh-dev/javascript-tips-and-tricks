from django.shortcuts import render,redirect
from .forms import UserCreationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


def user_register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            the_email = form.cleaned_data['email']
            the_full_name = form.cleaned_data['full_name']
            the_password = form.cleaned_data['password1']
            user = User.objects.create_user(the_email, the_password, the_full_name)
            user.save()
            login(request,user)
            messages.success(request, 'ثبت نام شما با موفقیت انجام شد','success')
            return redirect('doshop:home')
    else :
        form = UserCreationForm()
    context = {
        'form' : form ,
    }
    return render(request,'accounts/register.html',context)



def user_login(request):
    if request.method == 'POST' :
        form = UserLoginForm(request.POST)
        if form.is_valid() :
            the_email = form.cleaned_data['email']
            the_password = form.cleaned_data['password']
            user = authenticate(request, email=the_email, password=the_password)
            if user is not None :
                login(request,user)
                messages.success(request,'شما با موفقیت وارد شدید','success')
                return redirect('doshop:home')
            else :
                messages.error(request,'ایمیل یا رمز عبور ورودی صحیحی نمی باشد','danger')
    else :
        form = UserLoginForm()
    context = {
        'form' : form
    }
    return render (request,'accounts/login.html',context)



def user_logout(request):
    logout(request)
    messages.success(request,'شما با موفقیت از سیستم خارج شدید','success')
    return redirect('doshop:home')

