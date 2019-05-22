from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import (ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import dMenu, bMenu



def home(request):
    return render(request, 'main/home.html')

def contact(request):
    return render(request, 'main/contact.html')

def posts(request):
    context ={
    'post':dMenu.objects.all()
    }
    return render(request, 'main/dMenu.html', context)

def bPosts(request):
    context ={
    'bPost':dMenu.objects.all()
    }
    return render(request, 'main/bMenu.html', context)

class dMenuListView(ListView):
    model = dMenu
    template_name = 'main/dMenu.html'
    context_object_name = 'post'
    ordering = ['-date_posted']



class dMenuCreateView(LoginRequiredMixin,CreateView):
    model = dMenu
    fields = ['title','description', 'price' ]

class dMenuUpdateView(LoginRequiredMixin, UpdateView):
    model = dMenu
    fields = ['title', 'description', 'price']

class dMenuDeleteView(DeleteView):
    model = dMenu
    #redirect to the 2nd previous page
    success_url= ('../../')

#Beverage Menu

class bMenuListView(ListView):
    model = bMenu
    template_name = 'main/bMenu.html'
    context_object_name = 'bPost'
    ordering = ['-date_posted']


class bMenuCreateView(LoginRequiredMixin,CreateView):
    model = bMenu
    fields = ['bTitle','bDescription', 'bPrice' ]

class bMenuUpdateView(LoginRequiredMixin, UpdateView):
    model = bMenu
    fields = ['bTitle', 'bDescription', 'bPrice']

class bMenuDeleteView(DeleteView):
    model = bMenu
    #redirect to the 2nd previous page
    success_url= ('../../')
