from django.db import models
from django.core.validators import RegexValidator
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model

class Renter(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    buisiness_name = models.CharField(max_length=100)
    buisiness_liscence_number = models.CharField(max_length=20)
    PAN_card_number = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.user)
    
    def save(self,*args,**kwargs):
        super().save()
        self.user.profile.renter = True
        self.user.profile.save()
