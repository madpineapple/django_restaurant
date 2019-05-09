from django.urls import path
from .views import dMenuListView
from .import views


urlpatterns=[
    path('', views.home, name='main-home'),
    path('dMenu/',dMenuListView.as_view(), name='main-dMenu')
]
