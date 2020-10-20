from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('index/', views.strange, name="strange"),
    path('profile/',views.profile, name="profile"),
    path('profile/pricing/',views.pricing, name="pricing"),
    # path('profile/pricing/pay/',views.pay, name="pay"),
    path('pay/',views.pay, name="pay")
    # path('profile/pay/success/',views.success, name="success"),
]