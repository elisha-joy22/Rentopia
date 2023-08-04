from django import forms
from vehicle.models import Vehicle,VehicleCredentials


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make','model','type','seating_capacity','transmission','fuel_type','ex_showroom_price']


class VehicleCredentialsForm(forms.ModelForm):
    class Meta:
        model = VehicleCredentials
        fields = [
            'vehicle',
            'manufacturing_year',
            'registration_number',
            'insurance',
            'rc_book_and_paper',
            'mileage_in_km',
            'features',
            'available',
            'location',
            'image1'
            ]
        