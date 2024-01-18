# User/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('new-parcel/', views.new_parcel, name='user_new_parcel'),
    path('tracking/', views.tracking, name='user_tracking'),
    path('users-profile/', views.users_profile, name='user_users_profile'),
    path('pages-login/', views.pages_login, name='user_pages_login'),
    path('pages-register/', views.pages_register, name='user_pages_register'),
    path('pages-contact/', views.pages_contact, name='user_pages_contact'),
]
