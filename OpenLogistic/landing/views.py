from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Staff, Admin
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ParcelForm
from .models import Parcel
from django.http import JsonResponse


def index(request):
    return render(request, 'landing/index.html')

def new_parcel(request):
    return render(request, 'landing/new parcel.html')

def shipped(request):
    return render(request, 'landing/shipped.html')

def ship_pending(request):
    return render(request, 'landing/ship pending.html')

def delivery_pending(request):
    return render(request, 'landing/delivery pending.html')

# Admin views
def admin_index(request):
    return render(request, 'landing/admin index.html')

def admin_login_page(request):
    return render(request, 'landing/admin login.html')

def admin_profile(request):
    return render(request, 'landing/admin profile.html')

def admin_registration_page(request):
    return render(request, 'landing/admin reg.html')

def admin_staff(request):
    return render(request, 'landing/admin staff.html')

def admin_tracking(request):
    return render(request, 'landing/admin tracking.html')

# Staff views
def staff_index(request):
    return render(request, 'landing/staff index.html')

def staff_login_page(request):
    return render(request, 'landing/staff login.html')

def staff_profile(request):
    return render(request, 'landing/staff profile.html')

def staff_registration_page(request):
    return render(request, 'landing/staff reg.html')

def staff_tracking(request):
    return render(request, 'landing/staff tracking.html')

def staff_contact(request):
    return render(request, 'landing/staff contact.html')

# User views
def user_index(request):
    return render(request, 'landing/user index.html')

def user_registration_page(request):
    return render(request, 'landing/user reg.html')

def user_profile(request):
    return render(request, 'landing/user profile.html')

def user_tracking(request):
    return render(request, 'landing/user tracking.html')

def user_contact(request):
    return render(request, 'landing/user contact.html')

def user_login_page(request):
    return render(request, 'landing/user login.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('user index')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'landing/user login.html')

@login_required
def user_reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        nearby_branch = request.POST['nearby_branch']
        password = request.POST['password']

        user = CustomUser.objects.create_user(email=email, password=password)
        user.first_name = name
        user.near_by_branch = nearby_branch

        try:
            user.full_clean()  # Validate model fields
            user.save()

            # Log the user in after registration
            login(request, user)

            messages.success(request, 'Account created successfully!')
            return redirect('user index')
        except ValidationError as e:
            messages.error(request, f'Validation error: {e}')

    return render(request, 'landing/user reg.html')

@login_required
def staff_reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        branch = request.POST['branch']
        password = request.POST['password']
        email = request.POST['email']

        staff = CustomUser.objects.create_user(email=email, password=password)
        staff.first_name = name
        staff.near_by_branch = branch
        try:
            staff.full_clean()  # Validate model fields
            staff.save()

            messages.success(request, 'Staff account created successfully!')
            return redirect('staff index')
        except ValidationError as e:
            messages.error(request, f'Validation error: {e}')

    return render(request, 'landing/staff reg.html')

def staff_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        staff = authenticate(request, email=email, password=password)

        if staff is not None:
            login(request, staff)
            return redirect('staff index')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'landing/staff login.html')

@login_required
def admin_reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        branch = request.POST['branch']
        password = request.POST['password']
        email = request.POST['email']

        # Use your actual model for admin creation
        admin = CustomUser.objects.create_user(email=email, password=password)
        admin.first_name = name
        admin.near_by_branch = branch 

        try:
            admin.full_clean()  # Validate model fields
            admin.save()

            messages.success(request, 'Admin account created successfully!')
            return redirect('admin index')
        except ValidationError as e:
            messages.error(request, f'Validation error: {e}')

    return render(request, 'landing/admin reg.html')

def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        admin = authenticate(request, email=email, password=password)

        if admin is not None:
            login(request, admin)
            return redirect('admin index')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'landing/admin login.html')


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

def parcel_list(request):
    print('debuging')
    parcels = Parcel.objects.all()
    return render(request, 'Admin/a.html', {'parcels': parcels})

