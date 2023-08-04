'''
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from vehicle.models import Vehicle,Rent

@receiver(post_save,sender=Vehicle)
def add_rent(sender,instance,created,**kwargs):
    if created:
        rent_obj = Rent.objects.create(
            vehicle=instance    
        )
        rent_obj.set_fixed_price_and_per_km_rate()
        rent_obj.save()


@receiver(post_delete,sender=Vehicle)
def delete_rent(sender,instance,**kwargs):
    try:
        rent = get_object_or_404(Rent,vehicle=instance)
        rent.delete()
    except Rent.DoesNotExist:
        pass

        
'''    

