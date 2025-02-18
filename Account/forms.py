from django import forms
from .models import AbstractUser,Account_details
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Account_details
        fields=['username','first_name','last_name','email','password','phone_number']
    def save(self):
        s=super().save(commit=False)
        s.password=make_password(self.cleaned_data['password'])
        s.save()
        return s   
    
class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput())



class UpdateForm(forms.ModelForm):
    class Meta:
        model=Account_details
        fields=['username','first_name','last_name','email','phone_number']
    def save(self):
        s=super().save(commit=False)
        s.save()
        return s