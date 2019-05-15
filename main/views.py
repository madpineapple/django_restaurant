from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import dMenu



def home(request):
    return render(request, 'main/home.html')

def posts(request):
    context ={
    'post':dMenu.objects.all()
    }
    return render(request, 'main/dMenu.html', context)

class dMenuListView(ListView):
    model = dMenu
    template_name = 'main/dMenu.html'
    context_object_name = 'post'
    ordering = ['-date_posted']

class dMenuCreateView(CreateView):
    model = dMenu
    fields = ['title','description', 'price' ]

    



class dMenuUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = dMenu
    fields = ['title', 'description', 'price']
