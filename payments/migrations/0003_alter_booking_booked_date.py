# Generated by Django 4.2.3 on 2023-08-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_booking_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booked_date',
            field=models.DateTimeField(),
        ),
    ]
