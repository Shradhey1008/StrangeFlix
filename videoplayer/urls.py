from django.urls import path, include
from . import views

app_name = 'videoplayer'

urlpatterns = [
    path('youtube/', views.youtube_search, name='Utube_search'),  
    path('youtube/download/', views.youtube_down, name='Utube_down'),
    path('device/',views.DeviceUpload,name = 'DevUpload'),  
    path('device/<slug:slug>/',views.detail_view, name = 'detail'),  
    path('tag/<slug:slug>/',views.tagged,name = 'tagged'),  
    # path('upload/', views.upload, name='upload'),

    # path('index/', views.strange, name="strange"),
]