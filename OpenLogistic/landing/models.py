from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class User(models.Model):
    phone_number = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=255)
    near_by_branch = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    near_by_branch = models.CharField(max_length=255, blank=True)

    # Set related_name for groups and user_permissions directly on the fields
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    branch = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Staff ID: {self.staff_id}, Name: {self.name}"

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
    staff_assigned_detail = models.ForeignKey('landing.Staff', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Parcel ID: {self.parcel_id}, Status: {self.parcel_status}"
