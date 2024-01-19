# Generated by Django 4.2.4 on 2024-01-19 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('branch', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('parcel_id', models.AutoField(primary_key=True, serialize=False)),
                ('sender_name', models.CharField(max_length=255)),
                ('recipient_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('parcel_description', models.TextField()),
                ('parcel_weight', models.FloatField()),
                ('shipping_service', models.CharField(max_length=255)),
                ('from_branch', models.CharField(max_length=255)),
                ('to_branch', models.CharField(max_length=255)),
                ('parcel_status', models.CharField(max_length=255)),
                ('safe_product', models.BooleanField(default=False)),
                ('staff_assigned_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Staff.staff')),
            ],
        ),
    ]
