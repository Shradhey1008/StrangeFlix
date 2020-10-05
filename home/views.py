from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def strange(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def pay(request):
    return render(request,'pay.html')