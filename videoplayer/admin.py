from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import DeviceVideo

# registering Embed video model

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(DeviceVideo)