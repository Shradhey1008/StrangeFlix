from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('signup/', views.users_signup, name='signup'),
    # path('verify/',views.verify, name="verify"),  
]