# forms.py
from django import forms

class ParcelForm(forms.Form):
    sender_name = forms.CharField(max_length=255, required=True)
    sender_address = forms.CharField(widget=forms.Textarea, required=True)
    sender_phone = forms.CharField(max_length=15, required=True)
    from_branch = forms.ChoiceField(choices=[('1', 'Standard Service'), ('2', 'Express service'), ('3', 'Over Night Service')], required=True)

    recipient_name = forms.CharField(max_length=255, required=True)
    recipient_address = forms.CharField(widget=forms.Textarea, required=True)
    recipient_contact = forms.CharField(max_length=15, required=True)
    to_branch = forms.ChoiceField(choices=[('1', 'Standard Service'), ('2', 'Express service'), ('3', 'Over Night Service')], required=True)

    parcel_description = forms.CharField(widget=forms.Textarea, required=True)
    parcel_weight = forms.FloatField(required=True)
    shipping_service = forms.ChoiceField(choices=[('1', 'Standard Service'), ('2', 'Express service'), ('3', 'Over Night Service')], required=True)

    fragile = forms.BooleanField(required=False)
    terms = forms.BooleanField(required=False)
