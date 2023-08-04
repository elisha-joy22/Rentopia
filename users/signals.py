'''
from django.db.models.signals import post_save
from django.dispatch import receiver

from customers.models import Customer
from renters.models import Renter
from users.models import User

@receiver(post_save,sender=User)
def create_customer_or_renter(sender,instance,created,**kwargs):
    if created:
        if instance.is_customer:
            Customer.objects.create(user=instance)
        elif instance.is_renter:
            Renter.objects.create(user=instance)

'''
            
        

