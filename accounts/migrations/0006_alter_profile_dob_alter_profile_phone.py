# Generated by Django 4.2.3 on 2023-07-26 09:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_phone_number_profile_phone_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(verbose_name='DOB(dd/mm/yyyy)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]+$')], verbose_name='Phone Number'),
        ),
    ]
