# Generated by Django 4.2.3 on 2023-08-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='driving_liscence',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
