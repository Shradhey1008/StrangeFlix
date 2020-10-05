from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def signup(request):
    return render(request,'signup.html')

def verify(request):
    return render(request,'verify.html')

def users_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # phone = request.POST.get('phone')
        pass_1 = request.POST.get('password1')
        pass_2 = request.POST.get('password2')
        if pass_1 == pass_2:
             user = User.objects.create_user(
                                              username=email,
                                              email=email,
                                              password=pass_1,
                                             )
             return HttpResponseRedirect("/")
        else:
             error = " Password Mismatch "
             return render(request, 'signup.html',{"error":error})
    else:
         return render(request, 'signup.html')