from django.urls import path
from .views import index, new_parcel, shipped, ship_pending, delivery_pending
from .views import admin_index, admin_login_page, admin_profile, admin_registration_page, admin_staff, admin_tracking
from .views import staff_index, staff_login_page, staff_profile, staff_registration_page, staff_tracking, staff_contact
from .views import user_index, user_login_page, user_profile, user_registration_page, user_tracking, user_contact
from .views import user_reg, staff_reg, admin_reg, user_parcel_form_view, track_parcel_view, parcel_list

urlpatterns = [
    path('', index, name='index'),
    path('new-parcel/', new_parcel, name='new_parcel'),
    path('shipped/', shipped, name='shipped'),
    path('ship-pending/', ship_pending, name='ship_pending'),
    path('delivery-pending/', delivery_pending, name='delivery_pending'),

    # Admin URLs
    path('admin/', admin_index, name='admin_index'),
    path('admin/login/', admin_login_page, name='admin_login'),
    path('admin/profile/', admin_profile, name='admin_profile'),
    path('admin/registration/', admin_registration_page, name='admin_registration'),
    path('admin/staff/', admin_staff, name='admin_staff'),
    path('admin/tracking/', admin_tracking, name='admin_tracking'),

    # Staff URLs
    path('staff/', staff_index, name='staff_index'),
    path('staff/login/', staff_login_page, name='staff_login'),
    path('staff/profile/', staff_profile, name='staff_profile'),
    path('staff/registration/', staff_registration_page, name='staff_registration'),
    path('staff/tracking/', staff_tracking, name='staff_tracking'),
    path('staff/contact/', staff_contact, name='staff_contact'),

    # User URLs
    path('user/', user_index, name='user_index'),
    path('user/login/', user_login_page, name='user_login'),
    path('user/profile/', user_profile, name='user_profile'),
    path('user/registration/', user_registration_page, name='user_registration'),
    path('user/tracking/', user_tracking, name='user_tracking'),
    path('user/contact/', user_contact, name='user_contact'),

    path('ur/', user_reg, name='user_reg'),
    path('sr/', staff_reg, name='staff_reg'),
    path('ar/', admin_reg, name='admin_reg'),

    path('user/parcel-form/', user_parcel_form_view, name='user_parcel_form'),
    path('user/track-parcel/', track_parcel_view, name='track_parcel'),
    path('admin/parcel-list/', parcel_list, name='parcel_list'),
]
