from django.shortcuts import render,redirect, get_object_or_404
from .forms import UserCreationForm, UserLoginForm, UserEdit, UserChangePassForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


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



@login_required
def user_logout(request):
    logout(request)
    messages.success(request,'شما با موفقیت از سیستم خارج شدید','success')
    return redirect('doshop:home')



@login_required
def user_edit(request, user_id):
    the_user = get_object_or_404(User, id = user_id)
    if the_user.id == request.user.id:
        if request.method == 'POST' :
            print("post is run")
            form = UserEdit(request.POST, instance=the_user)
            if form.is_valid():
                fm = form.save(commit=False)
                fm.full_name = form.cleaned_data['full_name']
                fm.email = form.cleaned_data['email']
                fm.save()
                messages.success(request, 'ویرایش با موفقیت انجام شد', 'success')
                return redirect('accounts:user_profile', request.user.id)
                #return redirect('account:dashboard',user_id)
        else:
            form = UserEdit(instance = the_user)
        context = {'form': form}
        return render(request,'accounts/user_edit.html', context)
    else:
        return redirect('doshop:home')



@login_required
def user_profile(request, user_id):
    the_user = get_object_or_404(User, id = user_id)
    if the_user.id == request.user.id:
        context = {
            'the_user' : the_user
        }
        return render(request,'accounts/user_profile.html', context)
    else:
        return redirect('doshop:home')
    


@login_required
def user_change_pass(request, user_id):
    the_user = get_object_or_404(User, id = user_id)
    if the_user.id == request.user.id:
        if request.method == 'POST' :
            form = UserChangePassForm(request.POST, instance=the_user)
            if form.is_valid():
                fm = form.save(commit=False)
                fm.password1 = form.cleaned_data['password1']
                fm.save()
                login(request,the_user)
                messages.success(request, 'رمز عبور با موفقیت تغییر کرد', 'success')
                return redirect('accounts:user_profile', request.user.id)
        else:
            form = UserChangePassForm(instance = the_user)
        context = {'form': form}
        return render(request,'accounts/user_change_pass.html', context)
    else:
        return redirect('doshop:home')



# ------------------------------------ #
# Reset Password

class UserPassReset(auth_views.PasswordResetView):
    template_name = 'accounts/password/password_reset_form.html'
    success_url = reverse_lazy('accounts:reset_pass_done')
    email_template_name = 'accounts/password/password_reset_email.html'


class UserPassResetDone(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password/password_reset_done.html'


class UserPassResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:reset_pass_complete')


class UserPassResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password/password_reset_complete.html'




