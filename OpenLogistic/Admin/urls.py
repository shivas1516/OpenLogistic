# Admin/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin_index'),
    path('shipped/', views.shipped, name='admin_shipped'),
    path('delivery-pending/', views.delivery_pending, name='admin_delivery_pending'),
    path('ship-pending/', views.ship_pending, name='admin_ship_pending'),
    path('all-parcel/', views.all_parcel, name='admin_all_parcel'),
    path('tracking/', views.tracking, name='admin_tracking'),
    path('users-profile/', views.users_profile, name='admin_users_profile'),
    path('pages-login/', views.pages_login, name='admin_pages_login'),
    path('pages-register/', views.pages_register, name='admin_pages_register'),
    path('pages-contact/', views.pages_contact, name='admin_pages_contact'),
]