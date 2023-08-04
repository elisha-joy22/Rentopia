from django import forms
from django.forms import DateTimeInput

from payments.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_from','booking_till']
        widgets = {
            'booking_from': DateTimeInput(attrs={'type': 'datetime-local'}),
            'booking_till': DateTimeInput(attrs={'type': 'datetime-local'}),
        }