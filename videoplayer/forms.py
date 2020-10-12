from django import forms 
from .models import Video

# Creating new table in database as Video form
class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]