from django.contrib import admin
from vehicle import models

# Register your models here.
admin.site.register(models.Vehicle)
admin.site.register(models.VehicleCredentials)
admin.site.register(models.Rent)