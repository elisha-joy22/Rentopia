from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

import os
from datetime import date

from renters.models import Renter
from accounts.models import CustomUser

# Create your models here.


def rename_insurance_file(instance, filename):
    filename = f"{instance.registration_number}_insurance.pdf"
    return os.path.join(f'cars/{instance.registration_number}/documents', filename)

def rename_rc_book_and_paper(instance, filename):
    filename = f"{instance.registration_number}_rc_book&paper.pdf"
    return os.path.join(f'cars/{instance.registration_number}/documents', filename)


def rename_image_file(instance, filename):
    filename = f"{instance.registration_number}_rent_image.jpg"
    return os.path.join(f'cars/{instance.registration_number}/images', filename)




class Vehicle(models.Model):

    VEHICLE_TYPE = [
        ('SUV','SUV'),
        ('Sedan','Sedan'),
        ('Hatchback','Hatchback'),
        ('MPV','MPV')
    ]
    TRANSMISSION_TYPE=[
        ('Automatic','Automatic'),
        ('Manual','Manual')
    ]
    
    FUEL_TYPE=[
        ('Petrol','Petrol'),
        ('Diesel','Diesel'),
        ('Electric','Electric'),
        ('CNG','CNG'),
        ('Hybrid(Petrol)','Hybrid(Petrol)'),
        ('Hybrid(Diesel)','Hybrid(Diesel)')
    ]
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    type = models.CharField(max_length=20, choices=VEHICLE_TYPE)
    seating_capacity = models.PositiveIntegerField(default=2)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_TYPE)
    fuel_type = models.CharField(max_length=30, choices=FUEL_TYPE)
    ex_showroom_price = models.PositiveIntegerField(default=300000)
    #vehicle_default_image = models.ImageField(upload_to='cars/images/defaults/',default='cars/images/defaults')

    def calculate_class(self):
        if self.type=='SUV':
            if self.seating_capacity>=7:
                if self.ex_showroom_price>=1500000:
                    return "A"
                else:
                    return "B"
            else:
                return "C"
        elif self.type=='sedan':
            if self.ex_showroom_price_in_lakh>=2000000:
                return "A"
            elif self.ex_showroom_price_in_lakh>=1000000:
                return "B"
            else:
                return"C"
        elif self.type=='hatchback':
            if self.ex_showroom_price_in_lakh>=1500000:
                return "B"
            elif self.ex_showroom_price_in_lakh<=1500000:
                return "C"
            else:
                return "D"
    
    def __str__(self):
        return str(self.make + " " + self.model)




class VehicleCredentials(models.Model):
    renter = models.ForeignKey(Renter,on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    manufacturing_year = models.PositiveIntegerField()
    registration_number = models.CharField(max_length=14)
    insurance = models.FileField(
                    upload_to=rename_insurance_file,
                    validators=[
                        FileExtensionValidator(['pdf'])
                    ]
                )   
    rc_book_and_paper = models.FileField(
                    upload_to=rename_rc_book_and_paper,
                    validators=[
                        FileExtensionValidator(['pdf'])
                    ]
                )
    mileage_in_km = models.PositiveIntegerField()
    features = models.CharField(max_length=150)
    image1 = models.ImageField(
                default='default_car_pic.jpg',
                upload_to=rename_image_file
            )
    available = models.BooleanField(default=True)
    booked = models.BooleanField(default=False)
    location = models.CharField(max_length=50)

    def __str__(self):
        return str(self.registration_number)


class Rent(models.Model):
    vehicle = models.OneToOneField(Vehicle,on_delete=models.CASCADE)
    fixed_price_distance = 200
    fixed_price = models.PositiveIntegerField(default=2500)
    per_km_rate = models.PositiveIntegerField(default=18)

    def set_fixed_price_and_per_km_rate(self):
        if self.vehicle.calculate_class()=="A":
            self.fixed_price = 7000
            self.per_km_rate = 45
        elif self.vehicle.calculate_class()=="B":
            self.fixed_price = 6000
            self.per_km_rate = 35
        elif self.vehicle.calculate_class()=="C":
            self.fixed_price = 4000
            self.per_km_rate = 25
        elif self.vehicle.calculate_class()=="D":
            self.fixed_price = 2500
            self.per_km_rate = 18
        
    def calculate_price(self,distance):
        if distance<=self.fixed_price_distance:
            return self.fixed_price
        else:
            additional_distance = distance - self.fixed_price_distance
            additional_cost = additional_distance * self.per_km_rate
            return self.fixed_price + additional_cost
    
    def save(self,*args,**kwargs):
        self.set_fixed_price_and_per_km_rate()
        super().save(*args,**kwargs)

    def __str__(self):
        return str(self.vehicle)+' (Rent)'
    

