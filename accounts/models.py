from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager
)
from django.core.validators import RegexValidator


import os

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('User must have an email address!!')
        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self,email,password):
        if not email:
            raise ValueError('User must have an email address!')
        user = self.create_user(email,password=password)
        user.staff = True
        user.save(using=self._db)

    def create_superuser(self,email,password):
        if not email:
            raise ValueError('User must have an email address')
        user = self.create_user(email,password=password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)



class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name = 'email_address',
        max_length = 255,
        unique = True
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    def get_all_permissions(self):
        return [] 
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    objects = CustomUserManager()


def rename_image_file(instance, filename):
    filename = f"{instance.user.email}_pro_pic"
    return os.path.join(f'profile_pics/', filename)




class Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    username = models.CharField(max_length=50,null=True,blank=True,default=None)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField(verbose_name='DOB(dd/mm/yyyy)')
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^[0-9]+$')],
        verbose_name='Phone Number',
        unique=True
        )
    renter = models.BooleanField(default=False)
    driving_liscence = models.CharField(max_length=30,default=None,null=True,blank=True)
    profile_pic = models.ImageField(default='default_pro_pic.jpg',upload_to='profile_pics')
    

    @property
    def is_renter(self):
        return self.renter

    @property
    def get_renter_id(self):
        if self.renter:
            return self.user.renter

    @property
    def have_driving_liscence(self):
        if self.driving_liscence:
            return True
        return False
        
    def __str__(self):
        return str(self.user)