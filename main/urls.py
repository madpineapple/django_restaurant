from django.urls import path
from .views import (dMenuListView,
dMenuCreateView,
dMenuUpdateView,
dMenuDeleteView,
bMenuListView,
bMenuCreateView,
bMenuUpdateView,
bMenuDeleteView,
)
from .import views


urlpatterns=[
    path('', views.home, name='main-home'),
    path('contact/', views.contact, name='main-contact'),
    path('dMenu/',dMenuListView.as_view(), name='main-dMenu'),
    path('dMenu/new/',dMenuCreateView.as_view(), name='post-create'),
    path('dMenu/<int:pk>/update/',dMenuUpdateView.as_view(), name='post-update'),
    path('dMenu/<int:pk>/delete/',dMenuDeleteView.as_view(), name='post-delete'),
    #Beverge menu
    path('bMenu/',bMenuListView.as_view(), name='main-bMenu'),
    path('bMenu/new/',bMenuCreateView.as_view(), name='bPost-create'),
    path('bMenu/<int:pk>/update/',bMenuUpdateView.as_view(), name='bPost-update'),
    path('bMenu/<int:pk>/delete/',bMenuDeleteView.as_view(), name='bPost-delete')
]
