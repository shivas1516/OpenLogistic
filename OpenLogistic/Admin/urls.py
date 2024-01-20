# Admin/urls.py
from django.urls import path
from . import views
from .views import UserParcelFormView

urlpatterns = [
    path('', views.index, name='index'),
    path('shipped/', views.shipped, name='admin_shipped'),
    path('delivery-pending/', views.delivery_pending, name='admin_delivery_pending'),
    path('ship-pending/', views.ship_pending, name='admin_ship_pending'),
    path('all-parcel/', views.all_parcel, name='admin_all_parcel'),
    path('tracking/', views.admintracking, name='admin_tracking'),
    path('users-profile/', views.users_profile, name='admin_users_profile'),
    path('pages-login/', views.pages_login, name='admin_pages_login'),
    path('pages-register/', views.pages_register, name='admin_pages_register'),
    path('pages-contact/', views.pages_contact, name='admin_pages_contact'),
    path('submit_user_parcel_form/', UserParcelFormView.as_view(), name='submit_user_parcel_form'),
]