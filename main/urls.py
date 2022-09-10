from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('view', views.index, name='view')
]

