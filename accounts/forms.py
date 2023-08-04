from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from accounts.models import Profile


User = get_user_model()

class RegisterUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email already exists!!')
        return email
    
    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        cleaned_data = super().clean()

        if password is not None and password!=password2:
            raise forms.ValidationError("Passwords don't match")
        
        return cleaned_data
    

class UserAdminCreationForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput)

    
    class Meta:
        model = User
        fields = ['email']
     
    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        cleaned_data = super().clean()

        if password is not None and password!=password2:
            raise forms.ValidationError('Passwords dont match!')
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
    

class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField

    class Meta:
        model = User
        fields = ['email','password','is_active','admin']

    def clean_password(self):
        return self.initial['password']


class ProfileCreationForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Profile
        fields = ['first_name','last_name','dob','phone','profile_pic']

