from django.db import models
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


class DeviceVideo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnail/')
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    tags = TaggableManager()
    slug = models.SlugField(unique=True,max_length=100)


    def __str__(self):
        return self.title

class YTvideos(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnail/')
    thumbnail_url = models.URLField()
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    # tags = TaggableManager()
    slug = models.SlugField(unique=True,max_length=100)

    def get_remote_image(self):
        if self.thumbnail_url and not self.thumbnail:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.thumbnail_url).read())
            img_temp.flush()
            self.thumbnail.save(f"image_{self.pk}", File(img_temp))
        self.save()
    
    
         
