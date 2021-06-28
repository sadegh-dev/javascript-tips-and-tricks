
# -*- coding: utf-8 -*-
# Github.com/Rasooll
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
#from zeep import Client
from orders.models import Order
from django.contrib import messages



@login_required
def payment(request):
    # session for order
    if request.session.has_key('id_pay'):
        the_id = request.session['id_pay']
    the_order = Order.objects.get(id=the_id)  
    the_order.paid = True
    the_order.save()
    try:
        del request.session['id_pay']
    except:
        pass
    return redirect('orders:order_list')


@login_required
def verify(request):
    pass





"""
https://github.com/rasooll/zarinpal-django-py3


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
CallbackURL = 'http://localhost:8000/verify/' # Important: need to edit for realy server.
"""


"""
MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
description = "فروشگاه آنلاین"  # Required
CallbackURL = 'http://localhost:8000/zarinpal/verify/' # Important: need to edit for realy server.


@login_required
def payment(request):
    # session for order
    if request.session.has_key('id_pay'):
        the_id = request.session['id_pay']
    the_order = Order.objects.filter(id=the_id)
    email = the_order.user.email
    amount = the_order.total_price
    mobile = '9999999999' #request.user.mobile 

    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))



@login_required
def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        result.Status = 100 #TEST
        if result.Status == 100:
            if request.session.has_key('id_pay'):
                the_id = request.session['id_pay']
            order = Order.objects.get(id=the_id)
            order.paid = True
            order.save()
            try:
                del request.session['id_pay']
            except:
                pass
            messages.success(request, 'پرداخت با موفقیت انجام شد','success')
            return redirect('doshop:home')
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
"""
