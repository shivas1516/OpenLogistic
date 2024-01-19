from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def shipped(request):
    return render(request, 'shipped.html')

def delivery_pending(request):
    return render(request, 'delivery pending.html')

def ship_pending(request):
    return render(request, 'ship pending.html')

def all_parcel(request):
    return render(request, 'all parcel.html')

def admintracking(request):
    return render(request, 'admintracking.html')

def users_profile(request):
    return render(request, 'users-profile.html')

def pages_login(request):
    return render(request, 'pages-login.html')

def pages_register(request):
    return render(request, 'pages-register.html')

def pages_contact(request):
    return render(request, 'pages-contact.html')

