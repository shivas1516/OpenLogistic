# Generated by Django 4.2.4 on 2024-01-21 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
    ]