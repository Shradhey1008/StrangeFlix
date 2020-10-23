from django.db import models
from subscriptions.models import Membership
from videoplayer.models import DeviceVideo, YtVideo
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    allowed_membership = models.ManyToManyField(Membership)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category:detail", kwargs={"slug": self.slug})

    @property
    def videos(self):
        return self.video_set.all().order_by('position')



class Video(models.Model):
    slug = models.SlugField()
    device_video = models.ForeignKey(DeviceVideo,default=None,on_delete=models.CASCADE,null=True,blank=True)
    yt_video = models.ForeignKey(YtVideo,default=None,on_delete=models.CASCADE,null=True,blank=True)
    vid_category = models.ForeignKey(Category,on_delete=models.SET_NULL,null =True)
    position = models.IntegerField()
    
    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("category:video-detail", kwargs={"category_slug": self.vid_category.slug,"categoryvideo_slug":self.slug})