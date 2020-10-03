from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('index/', views.strange, name="strange"),
    path('signup/', views.signup, name="signup"),
    path('signup/verify/',views.verify, name="verify")
]