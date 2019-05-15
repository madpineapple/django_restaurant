from django.urls import path
from .views import dMenuListView, dMenuCreateView, dMenuUpdateView
from .import views


urlpatterns=[
    path('', views.home, name='main-home'),
    path('dMenu/',dMenuListView.as_view(), name='main-dMenu'),
    path('dMenu/new/',dMenuCreateView.as_view(), name='post-create'),
    path('dMenu/<int:pk>/update/',dMenuUpdateView.as_view(), name='post-update')
]
