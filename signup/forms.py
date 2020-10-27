from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from allauth.account.forms import SignupForm
from django import forms 
  
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


class SimpleSignupForm(SignupForm):
    phone = forms.CharField(max_length=12, label='Phone Number', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        user.phone = self.cleaned_data['phone']
        user.save()
        return user