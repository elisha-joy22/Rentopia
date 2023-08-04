
from django.shortcuts import render,redirect
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone

from vehicle.models import VehicleCredentials
from payments.forms import BookingForm


# Create your views here.
class BookingView(View):
    def get(self,request,pk):
        if not request.user.profile.have_driving_liscence:
            messages.error(request,'Please provide Driving liscence first!!')    
        vehicle = get_object_or_404(VehicleCredentials,id=pk)
        form = BookingForm
        return render(request,'payments/booking.html',{'vehicle':vehicle,'form':form})
    
    def post(self,request,pk):
        bookingform = BookingForm(request.POST)
        if not request.user.profile.have_driving_liscence and request.POST.get('driving_liscence')==['']:
            print("1")
            messages.error(request,'Please provide Driving liscence first!!')
            return redirect('vehicle-booking',pk=pk)
        if request.POST.get('driving_liscence')==['']:
            print("2")
            request.user.profile.driving_liscence = request.POST.get('driving_liscence')
            request.user.profile.save()
        if bookingform.is_valid():
            print("3")
            booking_instance = bookingform.save(commit=False)
            booking_instance.booked_date = timezone.now()
            booking_instance.user = request.user
            try:
                booking_instance.vehicle = VehicleCredentials.objects.get(id=pk)
                print("4")
            except:
                print("5")
                messages.error(request,'Vehicle not available - Booking failed!')
                return redirect('vehicle-list')
            print("6")
            if booking_instance.vehicle.available:
                booking_instance.vehicle.booked = True
                booking_instance.vehicle.save()
                booking_instance.booking_status = 'booked'
                booking_instance.save()
                messages.success(request,'Booking success!!')
                return redirect('my-bookings')
            return HttpResponse('Booking failed!!')

        