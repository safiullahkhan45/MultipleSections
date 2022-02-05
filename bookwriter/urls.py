from django.urls import path
from . import views

urlpatterns = [
    path('create_section/', views.create_section),
    path('get_section/', views.get_section),
    path('get_all_sections/', views.get_all_sections),
]