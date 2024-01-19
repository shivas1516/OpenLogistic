# Staff/models.py
from django.db import models
from Admin.models import Admin

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    branch = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Staff ID: {self.staff_id}, Name: {self.name}"
