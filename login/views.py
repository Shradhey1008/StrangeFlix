from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def login_page(request):
    return render(request,'signin.html')

def verify(request):
    return render(request,'verify.html')


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password1')
        # password = request.POST.get('password2')
        user = authenticate(username=email, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/users/home')
        else:
            error = " Sorry! Email and Password didn't match, Please try again ! "
            return render(request, 'signin.html',{'error':error})
    else:
        return render(request, 'signin.html')


def users_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass_1 = request.POST.get('password1')
        pass_2 = request.POST.get('password2')
        if pass_1 == pass_2:
             user = User.objects.create_user(
                                              username=phone,
                                              email=email,
                                              password=pass_1,
                                             )
             return HttpResponseRedirect("/")
        else:
             error = " Password Mismatch "
             return render(request, 'login/signup.html',{"error":error})
    else:
         return render(request, 'login/signup.html')