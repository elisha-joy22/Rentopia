from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^[0-9]+$')])
    dob = models.DateField(null=True)
    user_type = models.CharField(max_length=50,choices=[('customer','Customer'),('renter',"Renter"),('staff',"Staff"),('superuser',"Superuser")])

    
