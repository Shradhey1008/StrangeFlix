from django import forms 
from .models import DeviceVideo

# Creating new table in database as Video form
class DeviceVideoForm(forms.ModelForm):
    class Meta:
        model= DeviceVideo
        fields= ["title",'description', "videofile",'thumbnail','tags']