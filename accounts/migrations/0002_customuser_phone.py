# Generated by Django 4.2.3 on 2023-07-25 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default=987654321, max_length=10, unique=True, verbose_name='phone_number'),
            preserve_default=False,
        ),
    ]
