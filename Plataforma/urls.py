from django.contrib import admin
from django.urls import path
from .views import BaseView

urlpatterns = [
    path('plataform/', BaseView.as_view(), name='plataform')
]