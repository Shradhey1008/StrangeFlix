from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item ,DeviceVideo

# registering Embed video model

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
admin.site.register(DeviceVideo)