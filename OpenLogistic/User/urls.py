# User/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new-parcel/', views.new_parcel, name='new_parcel'),
    path('tracking/', views.tracking, name='tracking'),
    path('users-profile/', views.users_profile, name='users-profile'),
    path('pages-login/', views.pages_login, name='user_pages_login'),
    path('pages-register/', views.pages_register, name='user_pages_register'),
    path('pages-contact/', views.pages_contact, name='pages_contact'),
]
