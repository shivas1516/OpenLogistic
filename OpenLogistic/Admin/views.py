from django.shortcuts import render

def index(request):
    return render(request, 'Admin/index.html')

def shipped(request):
    return render(request, 'Admin/shipped.html')

def delivery_pending(request):
    return render(request, 'Admin/delivery pending.html')

def ship_pending(request):
    return render(request, 'Admin/ship pending.html')

def all_parcel(request):
    return render(request, 'Admin/all parcel.html')

def tracking(request):
    return render(request, 'Admin/tracking.html')

def users_profile(request):
    return render(request, 'Admin/users-profile.html')

def pages_login(request):
    return render(request, 'Admin/pages-login.html')

def pages_register(request):
    return render(request, 'Admin/pages-register.html')

def pages_contact(request):
    return render(request, 'Admin/pages-contact.html')

