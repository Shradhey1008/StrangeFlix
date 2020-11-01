from django.urls import path, include
from . import views
from subscriptions.views import cancelSubscription

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),  
    path('index/', views.strange, name="strange"),
    path('profile/',views.profile, name="profile"),
    path('profile/cancel/',cancelSubscription, name="cancel"),
    path('profile/pay/',views.pay, name="pay"),
    # path('videos/',views.Video,name = 'video')
]