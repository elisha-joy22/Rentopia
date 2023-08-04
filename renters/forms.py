from django import forms

from renters.models import Renter
from payments.models import Booking

class RenterProfileForm(forms.ModelForm):
    class Meta:
        model = Renter
        fields = ['buisiness_name','buisiness_liscence_number','PAN_card_number']

class CancelBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['cancellation_reason']