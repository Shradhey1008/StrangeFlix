from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.video, name='video'),  
    path('upload/', views.upload, name='upload'),  
    # path('index/', views.strange, name="strange"),
]