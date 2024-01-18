# Staff/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='staff_index'),
    path('tracking/', views.tracking, name='staff_tracking'),
    path('users-profile/', views.users_profile, name='staff_users_profile'),
    path('pages-login/', views.pages_login, name='staff_pages_login'),
    path('pages-register/', views.pages_register, name='staff_pages_register'),
    path('pages-contact/', views.pages_contact, name='staff_pages_contact'),
]
