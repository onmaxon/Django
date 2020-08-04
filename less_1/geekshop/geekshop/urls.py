# from django.contrib import admin
# from django.urls import path

from django.urls import path
from django.contrib import admin
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', mainapp.products, name='products'),

    path('products/all/', mainapp.products_all, name='products_all'),
    path('products/clothes/', mainapp.products_clothes, name='products_clothes'),
    path('products/another/', mainapp.products_another, name='products_another'),

    path('contact/', mainapp.contact, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
]

