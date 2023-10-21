"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from shop.views import *

urlpatterns = [
    path('', index),
    path('accounts/login/', login, name='login'),
    path('accounts/register/', register, name='register'),
    path('accounts/logout/', logout, name='logout'),

    path('profile/', show_profile, name='show_profile'),
    path('update-profile/', update_profile, name='update_profile'),

    path('product/', list_my_product, name='my_product'),
    path('create-product/', create_product, name='create_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('product/<uuid:id>/buy/', buy_product, name='buy_product'),

    path('featured/', list_featured_product, name='featured_product'),
    path('flag/', get_flag, name='get_flag'),
    path('report/<uuid:id>/', report_product, name='report_product'),

    path('tambah-duit-admin/', tambah_duit),
]
