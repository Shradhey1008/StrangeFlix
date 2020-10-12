from django.db import models
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    # upload = models.FieldFile(upload_to='videos/', null=True, verbose_name="")


class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)
    # class Meta:
    #     verbose_name = 'video'
    #     verbose_name_plural = 'videos'
         
