from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.users_signup, name='signup'),
    
]