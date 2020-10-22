from django.db import models
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


class DeviceVideo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnail/')
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    tags = TaggableManager()
    slug = models.SlugField(unique=True,max_length=100)


    def __str__(self):
        return self.title

    def products(self):
        return self.categoryvideo_set.all().order_by('position')

class YtVideo(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    thumbnail_url = models.URLField()
    ytubevideo = models.FileField(upload_to='videos/',null=True, verbose_name="")
    thumbnail = models.ImageField(upload_to='thumbnail/')
    # tags = TaggableManager()
    slug = models.SlugField(unique=True,max_length=100)

    def __str__(self):
        return self.title
    
    def products(self):
        return self.categoryvideo_set.all().order_by('position')

    
    
         
