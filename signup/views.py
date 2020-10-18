from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import requests
from django.http import JsonResponse
from django.contrib import messages
import random
from .forms import UserRegisterForm

# Create your views here.
data_session = ''

def signup(request):
    return render(request,'signup.html')

def users_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass_1 = request.POST.get('password')
        # pass_2 = request.POST.get('password2')
        print(username)
        print(email)
        print(phone)
        print(pass_1)
        user = authenticate(request, username=username, password=pass_1)
        if user:
            login(request, user)
            messages.success(request, f' wecome {username} !!')
            return HttpResponseRedirect("/")
        elif pass_1:
            
            api_key_anurag = '55c5a679-08bf-11eb-9fa5-0200cd936042'
            url = "http://2factor.in/API/V1/" +api_key_anurag+ "/SMS/" + phone + "/AUTOGEN/OTPSEND"
            response = requests.request("GET", url)
            data = response.json()
            global data_session
            data_session = data['Details']
            # otp_session_data is stored in session.
            user = User.objects.create_user(username=username,
                                              email=email,
                                              password=pass_1,
                                             )
            user.is_active = True
            user.save()
            return HttpResponseRedirect('/signup/verify/')
    else:
         return render(request, 'signup.html')


# To verify Phone number of the user using SMS otp verfication

def otp_verification(request):
    if request.method == 'POST':
        user_otp = request.POST['OTP']
        # print(user_otp)
        global data_session
        url = 'http://2factor.in/API/V1/55c5a679-08bf-11eb-9fa5-0200cd936042/SMS/VERIFY/' + data_session + "/" + user_otp + ""
        response = requests.request('GET',url)
        data = response.json()
        # print(data)
        if data['Status'] =='Success':
            return HttpResponseRedirect('/') 
        else:
            return render(request,'verify.html',{'message':'Wrong OTP'})
    else:
        return render(request,'verify.html')