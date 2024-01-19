# User/models.py
from django.db import models

class User(models.Model):
    phone_number = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=255)
    near_by_branch = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
