from django.urls import path
from . import views
from .models import Singers
from django.views.generic import ListView

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('handling/', views.handing_page, name='handling'),
]
