# Generated by Django 4.2.3 on 2023-08-04 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0007_remove_vehiclecredentials_availability_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclecredentials',
            name='booked',
            field=models.BooleanField(default=False),
        ),
    ]
