# Admin/models.py
from django.db import models

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    branch = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Parcel(models.Model):
    parcel_id = models.AutoField(primary_key=True)
    sender_name = models.CharField(max_length=255)
    sender_address = models.TextField()
    sender_phone = models.CharField(max_length=15)
    from_branch = models.CharField(max_length=255)

    recipient_name = models.CharField(max_length=255)
    recipient_address = models.TextField()
    recipient_contact = models.CharField(max_length=15)
    to_branch = models.CharField(max_length=255)

    parcel_description = models.TextField()
    parcel_weight = models.FloatField()
    shipping_service = models.CharField(max_length=255)
    sensitive_content = models.BooleanField(default=False, blank=True, null=True)


    parcel_status = models.CharField(max_length=255)
    staff_assigned_detail = models.ForeignKey('Staff.Staff', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Parcel ID: {self.parcel_id}, Status: {self.parcel_status}"
