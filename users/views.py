from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from users.forms import LoginForm
from payments.models import Booking

# Create your views here.
class MyBookingsView(View,LoginRequiredMixin):
    def get(self,request):
        bookings = Booking.objects.filter(user=request.user).order_by('-booked_date')
        return render(request,'user/my_bookings.html',{'bookings':bookings})

class BookingCancelView(View,LoginRequiredMixin):
    def get(self,request,pk):
        booking = get_object_or_404(Booking,id=pk)
        return render(request,'user/cancel_booking.html',{'booking':booking})
    
    def post(self,request,pk):
        booking = get_object_or_404(Booking,id=pk)
        if booking:
            booking.vehicle.booked = False
            booking.vehicle.save()
            booking.booking_status = 'cancelled_user'
            booking.save()
            messages.success(request,f"Booking {booking.id} cancelled successfully!")
            return redirect('my-bookings')
        else:
            messages.warning(request,f"Request cant be processed at the moment..Try again!")
            return redirect('cancel-booking')


