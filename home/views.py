from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def strange(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def verify(request):
    return render(request,'verify.html')