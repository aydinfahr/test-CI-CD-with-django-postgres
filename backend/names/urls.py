from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_name, name='add_name'),
    path('list/', views.list_names, name='list_names'),
]
