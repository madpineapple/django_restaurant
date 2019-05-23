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
# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# def statements for menu an home page

def home(request):
    return render(request, 'main/home.html')


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

# def statements for contact forms
# sendemail/views.py

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['example@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('../../')
    return render(request, "main/contact.html", {'form': form})



# classes

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
