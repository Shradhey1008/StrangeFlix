from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.users_signup, name='signup'),
    path('signup/',views.signup,name="signup"),
    path('signup/verify/',views.verify,name="verify"),
]