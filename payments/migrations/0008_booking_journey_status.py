# Generated by Django 4.2.3 on 2023-08-07 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_booking_cancellation_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='journey_status',
            field=models.CharField(choices=[('incomplete', 'Incomplete'), ('complete', 'Complete')], default='incomplete', max_length=20),
        ),
    ]