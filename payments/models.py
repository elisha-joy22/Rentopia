from django.db import models

from vehicle.models import VehicleCredentials
from accounts.models import CustomUser

# Create your models here.
class Booking(models.Model):
    vehicle = models.ForeignKey(VehicleCredentials,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    booking_from = models.DateTimeField()
    booking_till = models.DateTimeField()
    booked_date = models.DateTimeField()
    booking_status = models.CharField(max_length=25,
                                    choices=[
                                        ('booked','Booked'),
                                        ('cancelled_user','Cancelled By User'),
                                        ('cancelled_renter','Cancelled by Renter')
                                        ],
                                    default='booked'
                )
    cancellation_reason = models.CharField(max_length=50,default=None,null=True,blank=True)


    def __str__(self):
        return str(self.id)+" - "+str(self.vehicle)+ " by "+ str(self.user)
    
