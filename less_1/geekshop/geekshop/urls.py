from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', mainapp.products, name='products'),

    path('products/all/', mainapp.products_all, name='products_all'),
    path('products/clothes/', mainapp.products_clothes, name='products_clothes'),
    path('products/another/', mainapp.products_another, name='products_another'),

    path('contact/', mainapp.contact, name='contact'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('admin/', admin.site.urls, name='admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
