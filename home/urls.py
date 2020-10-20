from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('index/', views.strange, name="strange"),
    path('profile/',views.profile, name="profile"),
    path('profile/pay/',views.pay, name="pay"),
    path('success/',views.success, name="success"),
]