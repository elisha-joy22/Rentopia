from django.views.generic import View
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import RegisterUserForm, ProfileCreationForm
from accounts.models import Profile
from vehicle.models import VehicleCredentials

User = get_user_model()

class LoginUserView(View):
    def post(self,request):
        email = request.POST.get('username')
        password = request.POST.get('password')
        print(email)
        print(password)
        user = authenticate(request,email=email,password=password)
        if user != None:    
            login(request,user)
            #if user._is_customer:
            #    redirect('customer-home')
            #elif user._is_renter:
            #    redirect('renter-home')
            #else:
            return redirect('user-home')
        else:
            messages.error(request,'Login credentials invalid')
            return redirect("login")

    def get(self,request):
        if request.user.is_authenticated:
           return redirect('user-home')
        form = AuthenticationForm()
        return render(request,'accounts/login.html',{'form':form})
    
class RegisterUserView(View):
    def get(self,request):
        userform = RegisterUserForm
        profileform = ProfileCreationForm
        return render(request,'accounts/register.html',{'userform':userform,'profileform':profileform})
    def post(self,request):
        userform = RegisterUserForm(request.POST)
        profileform = ProfileCreationForm(request.POST)

        if userform.is_valid() and profileform.is_valid():
            email = userform.cleaned_data['email']
            password = userform.cleaned_data['password']
            new_user = User.objects.create_user(
                email=email,
                password=password
            )
            first_name = profileform.cleaned_data['first_name']
            last_name = profileform.cleaned_data['last_name']
            phone = profileform.cleaned_data['phone']
            dob = profileform.cleaned_data['dob']

            new_profile = Profile.objects.create(
                user=new_user,
                first_name=first_name,
                last_name=last_name,
                dob=dob,
                phone=phone
            )
            return redirect('user-login')
        else: 
            return redirect('user-register')
    
class LogoutUserView(View,LoginRequiredMixin):
    def get(self,request):
        logout(request)
        return redirect('user-login')
    

class ProfileView(View,LoginRequiredMixin):
    def get(self,request):
        profile_form = ProfileCreationForm(instance=request.user.profile)
        return render(request,'accounts/profile.html',{'user':request.user,'profile_form':profile_form})
    
    def post(self,request):
        profile_form = ProfileCreationForm(request.POST,request.FILES,instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Profile updated successfully!!')
            return redirect('user-profile')
        else:
            messages.error(request,'Profile update failed!!')
            return redirect('user-profile')


#@login_required
class HomeView(LoginRequiredMixin,View):
    def get(self,request):
        vehicles = VehicleCredentials.objects.all()
        print(vehicles)
        for vehicle in vehicles:
            print(vehicle.image1)
        return render(request,'home.html',{'vehicles':vehicles})

