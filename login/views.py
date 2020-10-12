from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.models import User
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import requests
from django.http import JsonResponse

# Create your views here.


def login_page(request):
    return render(request, 'signin.html')


# funtion to authenticate user in the database

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # password = request.POST.get('password2')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f' wecome {username} !!')
            return HttpResponseRedirect("/")
        else:
            error = " Sorry! Email and Password didn't match, Please try again ! "
            return render(request, 'signin.html', {'error': error})
    else:
        return render(request, 'signin.html')





