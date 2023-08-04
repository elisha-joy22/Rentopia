from django import forms
from users.models import User

class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['email','password1','password2']

