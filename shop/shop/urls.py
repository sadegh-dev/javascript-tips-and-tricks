"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('odrers/', include('orders.urls', namespace='orders')),
    path('api/', include('doapi.urls', namespace='doapi')),
    path('zarinpal/', include('zarinpal.urls', namespace='zarinpal')),
    path('api-token-auth/',obtain_auth_token, name='mytoken'),
    path('', include('doshop.urls', namespace='doshop')),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)  

# my b561b0532400ec4e371919df96da4c02ac33a609