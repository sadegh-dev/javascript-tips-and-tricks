
from django.urls import path
from . import views

"""
* way1 :
pip install zeep

* way2 :
pip install suds-py3

"""

app_name = 'zarinpal'


urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('verify/', views.verify , name='verify'),
]