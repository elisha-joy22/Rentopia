from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from vehicle.models import Vehicle,VehicleCredentials
from payments.models import Booking
from renters.models import Renter
from renters.forms import RenterProfileForm,CancelBookingForm

# Create your views here.
class home():
    def get(self,request):
        return HttpResponse('renters-home')
    


class RenterVehicleListView(ListView,LoginRequiredMixin):
    model = Vehicle
    template_name = 'vehicle/vehicle_list.html'
    context_object_name = 'vehicles'
    exclude_fields = ['renter']
    
    def get_queryset(self):
        return VehicleCredentials.objects.filter(renter=Renter.objects.get(user=self.request.user))
    
class RenterRegisterView(View,LoginRequiredMixin):
    def get(self,request):
        if request.user.profile.is_renter:
            renter_profile_form =  RenterProfileForm(instance=request.user.renter)
            return render(request,'accounts/renter_profile.html',{renter_profile_form:renter_profile_form})
        renter_profile_form =  RenterProfileForm()
        return render(request, 'accounts/renter_profile.html', {'renter_profile_form':renter_profile_form})

    def post(self,request):
        if request.user.profile.renter:
            renter_profile_form = RenterProfileForm(request.POST,instance=request.user.renter)
        else:
            renter_profile_form = RenterProfileForm(request.POST) 
        if renter_profile_form.is_valid():
            renter_profile_form.instance.user = request.user
            renter_profile_form.save()
            messages.success(request,'Renter details updated successfully!')
            return redirect('renter-register-profile')
        else:
            messages.error(request,'Updating Renter details failed!')
            return redirect('renter-register-profile')


class ViewBookingsView(View,LoginRequiredMixin):
    def get(self,request,pk):
        vehicle = VehicleCredentials.objects.get(id=pk)
        print(vehicle)
        bookings = Booking.objects.filter(vehicle=vehicle).order_by('-booked_date')
        return render(request,'renter/view_bookings.html',{'bookings':bookings})


class CancelBookingView(View,LoginRequiredMixin):
    def get(self,request,pk):
        booking = get_object_or_404(Booking,id=pk)
        if booking:
            cancel_form = CancelBookingForm()
            return render(request,'renter/cancel_booking.html',{'booking':booking,'cancel_form':cancel_form})
        messages.error(request,"Bad request")
        return redirect(request,'my-vehicles')
    
    def post(self,request,pk):
        print('in post')
        booking = get_object_or_404(Booking,id=pk)
        if not booking:
            messages.error(request,"Request cant be processed right now!! please check booking id")
            return redirect('cancel-booking-renter')
        cancel_form = CancelBookingForm(request.POST)
        if cancel_form.is_valid():
            cancellation_reason = cancel_form.cleaned_data.get('cancellation_reason')
            booking.vehicle.booked = False
            booking.vehicle.save()
            booking.booking_status = 'cancelled_renter'
            booking.cancellation_reason = cancellation_reason
            booking.save()
            messages.success(request,'Booking cancelled successfully!')
            return redirect('view-bookings', pk=booking.vehicle.id)
        messages.error(request,'Please provide in correct format')


class MyBookingsRenterView(View,LoginRequiredMixin):
    def get(self,request):
        renter = Renter.objects.get(user=request.user)
        vehicle = VehicleCredentials.objects.filter(renter=renter,booked=True)
        bookings = Booking.objects.filter(vehicle__in=vehicle,booking_status='booked')
        print(vehicle)
        print(bookings)
        return render(request,'renter/my-bookings.html',{'bookings':bookings})