from rest_framework import serializers
from vehicle.models import VehicleCredentials,Vehicle
from renters.models import Renter
from django.core.validators import FileExtensionValidator


class VehicleCredentialsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    renter_id = serializers.PrimaryKeyRelatedField(queryset=Renter.objects.all())
    vehicle_id = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())
    manufacturing_year = serializers.IntegerField()
    registration_number = serializers.CharField(max_length=14)
    insurance = serializers.FileField(
                    max_length=None, allow_empty_file=False, use_url=True,
                    validators=[FileExtensionValidator(['pdf'])]
                )
    rc_book_and_paper = serializers.FileField(
                    max_length=None, allow_empty_file=False, use_url=True,
                    validators=[FileExtensionValidator(['pdf'])]
                )
    mileage_in_km = serializers.IntegerField()
    features = serializers.CharField(max_length=150)
    image1 = serializers.ImageField(
                default='default_car_pic.jpg',
                max_length=None, allow_empty_file=True, use_url=True
            )
    available = serializers.BooleanField(default=True)
    booked = serializers.BooleanField(default=False)
    location = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return VehicleCredentials.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
class VehicleCredentialModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCredentials
        fields = ['renter','vehicle','registration_number']
