# Staff/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'Staff/index.html')

def tracking(request):
    return render(request, 'Staff/tracking.html')

def users_profile(request):
    return render(request, 'Staff/users-profile.html')

def pages_login(request):
    return render(request, 'Staff/pages-login.html')

def pages_register(request):
    return render(request, 'Staff/pages-register.html')

def pages_contact(request):
    return render(request, 'Staff/pages-contact.html')
