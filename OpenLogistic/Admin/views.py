from django.shortcuts import render
from django.views import View
from Admin.models import Parcel
from django.http import HttpResponse


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

class UserParcelFormView(View):
    def post(self, request, *args, **kwargs):
        try:
            # Extract form data from the request
            sender_name = request.POST.get('senderName')
            sender_address = request.POST.get('senderTextarea')
            sender_phone = request.POST.get('senderNumber')
            from_branch = request.POST.get('from')

            recipient_name = request.POST.get('recipientName')
            recipient_address = request.POST.get('recipientTextarea')
            recipient_contact = request.POST.get('recipientNumber')
            to_branch= request.POST.get('to_branch')

            parcel_description = request.POST.get('parcelTextarea')
            parcel_weight = request.POST.get('parcelNumber1')
            shipping_service = request.POST.get('shippingService')
            fragile = request.POST.get('fragile')

        # Set default values for certain fields
            parcel_status = "Shipping Pending" 
            staff_assigned_detail_id = None  
            safe_product = False  

        # Validate the form data (you can customize the validation based on your requirements)
            if not sender_name or not sender_address or not sender_phone or not from_branch \
                or not recipient_name or not recipient_address or not recipient_contact or not to_branch \
                or not parcel_description or not parcel_weight or not shipping_service:
                return HttpResponse('Form submission failed. Please fill in all required fields.')

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
                safe_product=bool(fragile),
            )
            parcel.save()
        # Redirect to a success page or do something else
            return HttpResponse('Form submitted successfully!')
        except Exception as e:
            # Print or log the exception for debugging
            print(f"Form submission error: {e}")
            return HttpResponse('Form submission failed. Please try again.')
