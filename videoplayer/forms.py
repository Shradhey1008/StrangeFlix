from django import forms 
from .models import DeviceVideo, YtVideo

# Creating new table in database as Video form
class DeviceVideoForm(forms.ModelForm):
    class Meta:
        model= DeviceVideo
        fields= ["title",'description', "videofile",'thumbnail','tags']

class YTvideoForm(forms.ModelForm):
    class Meta:
        model = YtVideo
        fields = ["title",'description', "ytubevideo",'thumbnail_url']