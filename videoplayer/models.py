from django.db import models
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    # upload = models.FieldFile(upload_to='videos/', null=True, verbose_name="")


class DeviceVideo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnail/')
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    tags = TaggableManager()
    slug = models.SlugField(unique=True,max_length=100)


    def __str__(self):
        return self.title

    
         
