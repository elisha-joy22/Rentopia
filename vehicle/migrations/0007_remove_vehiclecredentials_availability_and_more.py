# Generated by Django 4.2.3 on 2023-08-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0006_alter_vehiclecredentials_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclecredentials',
            name='availability',
        ),
        migrations.AddField(
            model_name='vehiclecredentials',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
