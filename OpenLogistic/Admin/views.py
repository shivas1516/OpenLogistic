from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ParcelForm
from .models import Parcel

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

@csrf_exempt  # Use this decorator if CSRF validation is causing issues for testing purposes
def user_parcel_form_view(request):
    print("View function called")  # For debugging purposes
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            # Extract form data from the validated form
            sender_name = form.cleaned_data['sender_name']
            sender_address = form.cleaned_data['sender_address']
            sender_phone = form.cleaned_data['sender_phone']
            from_branch = form.cleaned_data['from_branch']

            recipient_name = form.cleaned_data['recipient_name']
            recipient_address = form.cleaned_data['recipient_address']
            recipient_contact = form.cleaned_data['recipient_contact']
            to_branch = form.cleaned_data['to_branch']

            parcel_description = form.cleaned_data['parcel_description']
            parcel_weight = form.cleaned_data['parcel_weight']
            shipping_service = form.cleaned_data['shipping_service']
            fragile = form.cleaned_data['fragile']

            # Set default values for certain fields
            parcel_status = "Shipping Pending"
            staff_assigned_detail_id = None
            safe_product = fragile

            # Create and save a Parcel instance
            parcel = Parcel(
                sender_name=sender_name,
                sender_address=sender_address,
                sender_phone=sender_phone,
                from_branch=from_branch,
                recipient_name=recipient_name,
                recipient_address=recipient_address,
                recipient_contact=recipient_contact,
                to_branch=to_branch,
                parcel_description=parcel_description,
                parcel_weight=parcel_weight,
                shipping_service=shipping_service,
                parcel_status=parcel_status,
                staff_assigned_detail_id=staff_assigned_detail_id,
                safe_product=safe_product,
            )
            parcel.save()

            # Redirect to a success page or do something else
            return HttpResponse('Form submitted successfully!')
        else:
            # Print form errors for debugging purposes
            print(form.errors)
            # Return the form errors in the response
            return HttpResponse(f'Form submission failed. Please check the form for errors. Errors: {form.errors}')
    else:
        # You need to define the form instance here for the GET request
        form = ParcelForm()
        return render(request, 'index.html', {'form': form})
