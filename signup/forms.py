from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
  
  
# A Custom user registration form with added fields
class UserRegisterForm(UserCreationForm):
 
    username = forms.CharField(max_length = 20) 
    password = forms.CharField(max_length=20)
    email = forms.EmailField() 
    phone_no = forms.CharField(max_length = 20) 
    # first_name = forms.CharField(max_length = 20) 
    # last_name = forms.CharField(max_length = 20)
    class Meta: 
        model = User 
        fields = ['username', 'email', 'phone_no', 'password1','password2'] 