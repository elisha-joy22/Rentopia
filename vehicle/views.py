from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse
from django.views.generic import View,ListView,DetailView
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

import os


from vehicle.models import Vehicle,VehicleCredentials,Rent
from vehicle.forms import VehicleForm,VehicleCredentialsForm
from accounts.models import CustomUser
from renters.models import Renter
from payments.models import Booking

User = get_user_model()

# Create your views here.
class VehicleListView(ListView,LoginRequiredMixin):
    model = Vehicle
    template_name = 'vehicle/vehicle_list.html'
    context_object_name = 'vehicles'
    
    #def get_queryset(self):
    #    return Vehicle.objects.filter(availability='available')

class VehicleCredentialListView(ListView,LoginRequiredMixin):
    model = VehicleCredentials
    template_name = 'vehicle/vehicle_credential_list.html'
    context_object_name = 'vehicle_credentials'

    def get_queryset(self):
        return VehicleCredentials.objects.filter(renter_id__user=self.request.user)
   
class VehicleCredentialDetailView(DetailView,LoginRequiredMixin):
    model = VehicleCredentials
    template_name = 'vehicle/vehicle_credential_detail.html'
    context_object_name = 'vehicle_credential'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return VehicleCredentials.objects.filter(id=pk)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        vehicle = self.object
        booking = Booking.objects.filter(vehicle=vehicle,booking_status='booked').order_by('-booking_till').first()
        context['booking'] = booking 
        return context   


def download_documents_pdf(request,kl_number,pdf_type):
    # Specify the path to the PDF file in the "cars" directory
    pdf_type = '_'+pdf_type+'.pdf'
    pdf_file_path = os.path.join(settings.BASE_DIR,'media','cars',kl_number,'documents',kl_number.replace(' ','_')+pdf_type)
    # Check if the file exists
    if os.path.exists(pdf_file_path):
        # Open the file and serve it as a response
        with open(pdf_file_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="insurance_policy.pdf"'
            return response
    else:
        # Return a 404 page if the file does not exist
        return HttpResponse('The requested file does not exist.', status=404)


class VehicleFormView(View,LoginRequiredMixin):
    def get(self,request):
        vehicle_form = VehicleForm
        return render(request,'vehicle/vehicle_form.html',{'vehicle_form':vehicle_form})

    def post(self,request):
        vehicle_form = VehicleForm(request.POST)
        renter = None
        try:
            renter = Renter.objects.get(user=request.user)
            if not renter:
                return HttpResponse('Sign up as a renter to use this feature!')        
        except:
            print('Renter query failed!')

        if vehicle_form.is_valid():
            type = vehicle_form.cleaned_data.get('type')
            make = vehicle_form.cleaned_data.get('make')
            model = vehicle_form.cleaned_data.get('model')
            model_year = vehicle_form.cleaned_data.get('model_year')
            seating_capacity = vehicle_form.cleaned_data.get('seating_capacity')
            transmission = vehicle_form.cleaned_data.get('transmission')
            fuel_type = vehicle_form.cleaned_data.get('fuel_type')

            Vehicle.objects.create(
                renter = renter,
                type = type,
                make = make,
                model = model,
                model_year = model_year,
                seating_capacity = seating_capacity,
                transmission = transmission,
                fuel_type = fuel_type
            )
        return redirect('renter-vehicle-list')




class VehicleCredentialView(View,LoginRequiredMixin):
    def get(self,request):
        vehicle_credential_form = VehicleCredentialsForm
        return render(request,'vehicle/vehicle_credential_form.html',{'vehicle_credential_form':vehicle_credential_form})
    
    def post(self,request):
        vehicle_credential_form = VehicleCredentialsForm(request.POST,request.FILES)
        print(vehicle_credential_form)
        if request.user.profile.renter:
            print('1')
            if vehicle_credential_form.is_valid():
                print('2')
                vehicle_credential_form.instance.renter = request.user.renter
                vehicle_credential_form.save()
                messages.success(request,'Successfully added Vehicle')
                return redirect('renter-vehicle-list')
            else:
                print('3')
                messages.error(request,'Provide valid details')
                return redirect('add-vehicle-credential')
        print('4')
        messages.error(request,'Sign up as a renter  to add vehicle')
        return redirect('renter-register-profile')


class VehicleDeleteView(View,LoginRequiredMixin):
    def get(self,request,pk):
        vehicle_credential_id = pk
        try:
            vehicle_credential = VehicleCredentials.objects.get(id=vehicle_credential_id) 
        except:
            return HttpResponse("This action can't be completed right now!")
        vehicle = {
            'id':vehicle_credential.id,
            'registration_number':vehicle_credential.registration_number,
            'make_and_model':vehicle_credential.vehicle.make + vehicle_credential.vehicle.model,
            'image1':vehicle_credential.image1
        }
        return render(request,'vehicle/vehicle_delete_confirm.html',{'vehicle':vehicle})
    
    def post(self,request,pk):
        vehicle_credential = VehicleCredentials.objects.get(id=pk)
        vehicle_credential.delete()
        messages.success(request,'Vehicle and details was deleted successfully!')
        return redirect('vehicle-list')
    
