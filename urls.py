from django.contrib import admin
from django.urls import path
from .views import index, predict
urlpatterns = [
    path('index/', index, name='index'),
    path('', predict, name='predict'),
]
