from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView
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
