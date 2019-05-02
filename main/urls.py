from django.urls import path
from .import views

urlpatterns=[
    path('', views.home, name='main-home'),
    path('dMenu/',views.dMenu, name='main-dMenu')
]
