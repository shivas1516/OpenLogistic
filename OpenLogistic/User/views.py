# User/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'User/index.html')

def new_parcel(request):
    return render(request, 'User/new parcel.html')

def tracking(request):
    return render(request, 'User/tracking.html')

def users_profile(request):
    return render(request, 'User/users-profile.html')

def pages_login(request):
    return render(request, 'User/pages-login.html')

def pages_register(request):
    return render(request, 'User/pages-register.html')

def pages_contact(request):
    return render(request, 'User/pages-contact.html')
