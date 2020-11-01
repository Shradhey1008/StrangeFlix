from django.shortcuts import render
from .models import DeviceVideo, YtVideo
from django.core.files.storage import FileSystemStorage
from .forms import DeviceVideoForm
from pytube import YouTube
from django.conf import settings
from django.template.defaultfilters import slugify
from taggit.models import Tag
from django.shortcuts import get_object_or_404
import os
# Create your views here.


def DeviceUpload(request):
    form = DeviceVideoForm(request.POST, request.FILES)
    if form.is_valid():
        newvideo = form.save(commit=False)
        newvideo.slug = slugify(newvideo.title)
        title = newvideo.title.replace(' ','_').replace("|","_").replace("?","_").replace("*","_").replace('"','_').replace(':','_')
        newvideo.title = title
        newvideo.save()
        form.save_m2m()

    videofiles = DeviceVideo.objects.order_by('title')
    print([video.videofile.name for video in videofiles ])
    # Show most common tags
    common_tags = DeviceVideo.tags.most_common()[:4]
    context = {
        'videos': videofiles,
        'common_tags': common_tags,
        'form': form,
    }
    return render(request, 'device.html', context)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name
    video = DeviceVideo.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'videos': video,
    }

    return render(request, 'device.html', context)


def detail_view(request, slug):
    video = get_object_or_404(DeviceVideo, slug=slug)
    context = {
        'video': video,
    }
    return render(request, 'detail.html', context)


def youtube_search(request):
    if request.method == 'POST':
        video_url = request.POST['video_url']
        yt = YouTube(video_url)
        title = yt.title
        thumbnail_url = yt.thumbnail_url
        res = render(request, 'youtube.html', {
                     "title": title, "thumbnail_url": thumbnail_url, "video_url": video_url})
        return res
    else:
        return render(request, 'youtube.html')


def youtube_down(request):
    if request.method == 'POST':
        formatRadio = request.POST.get('formatRadio')
        if formatRadio != "audio":
            qualityRadio = request.POST.get('qualityRadio')
        video_url_d = request.POST.get('video_url_d')
        print(formatRadio)
        yt = YouTube(str(video_url_d))
        title = yt.title.replace(' ','_').replace("|","_").replace("?","_").replace("*","_").replace('"','_').replace(':','_')
        ytpath = 'videos/' + title + '.mp4'
        print(ytpath)
        # print('Downloading has started....')
        if formatRadio == "audio":
            yt.streams.filter(type=formatRadio).last().download(settings.MEDIA_ROOT)
        else:
            yt.streams.filter(type = formatRadio,resolution=qualityRadio).first().download(settings.MEDIA_ROOT + '/videos/',title)
        # print("Downloding completed")

        youtube_form = YtVideo(title=title,description=yt.description,thumbnail_url=yt.thumbnail_url,slug = slugify(title))
        youtube_form.ytubevideo.name = ytpath
        youtube_form.save()
    return render(request,'youtube.html',{"msg":"downloading completed"}) 