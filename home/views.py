from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')

def strange(request):
    return render(request, 'index.html')

# @login_required
def profile(request):
    return render(request, 'profile.html')

def pricing(request):
    return render(request,'pricing.html')

def success(request):
    return render(request,'success.html')

def pay(request):
    return render(request,'pay.html')