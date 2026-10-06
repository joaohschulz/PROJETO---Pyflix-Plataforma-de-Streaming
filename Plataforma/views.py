from django.shortcuts import render
from django.views.generic import ListView
from .models import Episodios
from django.contrib.auth.mixins import LoginRequiredMixin 

class BaseView(LoginRequiredMixin, ListView):
    template_name = 'base_plataform.html'
    model = Episodios
    context_object_name = 'episodios'
    
