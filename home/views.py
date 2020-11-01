from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from subscriptions.views import get_user_membership, get_user_subscription
# Create your views here.

def index(request):
    return render(request, 'index.html')

def strange(request):
    return render(request, 'index.html')

# @login_required
def profile(request):
    user_membership = get_user_membership(request)
    user_subscription = get_user_subscription(request)
    context = {
        'user_membership':user_membership,
        'user_subscription':user_subscription,
    }

    return render(request, 'profile.html',context)

def pay(request):
    return render(request,'pay.html')

# def Video(request):
#     return render(request,'video.html')