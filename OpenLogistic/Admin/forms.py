# forms.py
from django import forms

class ParcelForm(forms.Form):
    sender_name = forms.CharField(max_length=255, required=True)
    sender_address = forms.CharField(widget=forms.Textarea, required=True)
    sender_phone = forms.CharField(max_length=15, required=True)
    from_branch = forms.ChoiceField(choices=[
    ('Nungambakkam, Chennai', 'Nungambakkam, Chennai'),
    ('Guindy, Chennai', 'Guindy, Chennai'),
    ('Anna Nagar, Chennai', 'Anna Nagar, Chennai')
], required=True)

    recipient_name = forms.CharField(max_length=255, required=True)
    recipient_address = forms.CharField(widget=forms.Textarea, required=True)
    recipient_contact = forms.CharField(max_length=15, required=True)
    to_branch = forms.ChoiceField(choices=[
    ('Old Bus Stant, Thanjavur', 'Old Bus Stant, Thanjavur'),
    ('Rajan Road, Thanjavur', 'Rajan Road, Thanjavur'),
    ('South Rampart, Thanjavur', 'South Rampart, Thanjavur'),
    ('New Bus Stant, Thanjavur', 'New Bus Stant, Thanjavur')
], required=True)

    parcel_description = forms.CharField(widget=forms.Textarea, required=True)
    parcel_weight = forms.FloatField(required=True)
    shipping_service = forms.ChoiceField(choices=[
    ('Standard Service', 'Standard Service'),
    ('Express service', 'Express service'),
    ('Over Night Service', 'Over Night Service')
], required=True)

    sensitive_content= forms.CharField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        required=False
    )

