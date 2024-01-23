# Generated by Django 4.2.4 on 2024-01-23 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_remove_customuser_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('parcel_id', models.AutoField(primary_key=True, serialize=False)),
                ('sender_name', models.CharField(max_length=255)),
                ('sender_address', models.TextField()),
                ('sender_phone', models.CharField(max_length=15)),
                ('from_branch', models.CharField(max_length=255)),
                ('recipient_name', models.CharField(max_length=255)),
                ('recipient_address', models.TextField()),
                ('recipient_contact', models.CharField(max_length=15)),
                ('to_branch', models.CharField(max_length=255)),
                ('parcel_description', models.TextField()),
                ('parcel_weight', models.FloatField()),
                ('shipping_service', models.CharField(max_length=255)),
                ('sensitive_content', models.BooleanField(blank=True, default=False, null=True)),
                ('parcel_status', models.CharField(max_length=255)),
                ('staff_assigned_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='landing.staff')),
            ],
        ),
    ]