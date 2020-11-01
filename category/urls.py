from django.urls import path, include
from . import views

app_name = 'category'

urlpatterns = [
    path('',views.CategoryList,name = 'list'),
    path('comment/',views.videoComments,name = 'video-comment'),
    path('<slug:slug>/',views.CategoryView,name = 'detail'),
    path('<category_slug>/<categoryvideo_slug>/',views.Category_video,name = 'video-detail'),
]