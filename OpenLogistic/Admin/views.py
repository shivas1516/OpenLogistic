from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ParcelForm
from .models import Parcel
from django.http import JsonResponse

def my_view(request):
    data = {'key': 'value'}
    return JsonResponse(data)


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
            sensitive_content = form.cleaned_data['sensitive_content']
            sensitive_content = True if sensitive_content else False

            # Set default values for certain fields
            parcel_status = "Shipping Pending"
            staff_assigned_detail_id = None

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
                sensitive_content=sensitive_content,
            )
            parcel.save()

            # Redirect to a success page or render a template
            return render(request, 'User/index.html')
        else:
            # Print form errors for debugging purposes
            print(form.errors)
            # Return the form errors in the response
            return HttpResponse(f'Form submission failed. Please check the form for errors. Errors: {form.errors}')
    else:
        return HttpResponse('Invalid request method. Only POST is allowed for this view.')
    

@csrf_exempt  # Use this decorator if CSRF validation is causing issues for testing purposes
def track_parcel_view(request):
    if request.method == 'POST':
        # Get the entered parcel ID from the form
        parcel_id = request.POST.get('trackingCode')

        try:
            # Query the database for the Parcel with the entered ID
            parcel = Parcel.objects.get(parcel_id=parcel_id)

            # Prepare data to be sent to the template
            data = {
                'parcel_id': parcel.parcel_id,
                'parcel_status': parcel.parcel_status,
                'sender_name': parcel.sender_name,
                'sender_address': parcel.sender_address,
                'sender_phone': parcel.sender_phone,
                'from_branch': parcel.from_branch,
                'recipient_name': parcel.recipient_name,
                'recipient_address': parcel.recipient_address,
                'recipient_contact': parcel.recipient_contact,
                'to_branch': parcel.to_branch,
                'parcel_description': parcel.parcel_description,
                'parcel_weight': parcel.parcel_weight,
                'shipping_service': parcel.shipping_service,
                'staff_assigned_detail': parcel.staff_assigned_detail,
                'sensitive_content': parcel.sensitive_content,
            }

            # Return the data as JSON response
            return JsonResponse(data)
        except Parcel.DoesNotExist:
            # If the Parcel with the entered ID does not exist, return an error message
            return JsonResponse({'error': 'Parcel not found'})
    else:
        # If the request method is not POST, return an error message
        return JsonResponse({'error': 'Invalid request method. Only POST is allowed for this view.'})

