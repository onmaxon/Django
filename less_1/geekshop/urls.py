from django.urls import path, include

path('auth/', include('authapp.urls', namespace='auth'))
