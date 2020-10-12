
from django.contrib import admin 
from django.urls import path, include 
from login import views as user_view 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'),name = 'home'),
    path('login/',include('login.urls'), name = 'signin'),
    path('signup/',include('signup.urls'), name = 'signup'),
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
    path('accounts/', include('allauth.urls')),
    path('video/',include('videoplayer.urls'),name='videoplayer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
