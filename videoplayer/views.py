from django.shortcuts import render
from .models import DeviceVideo,YTvideos
from django.core.files.storage import FileSystemStorage
from .forms import DeviceVideoForm
from pytube import YouTube
from django.conf import settings
from django.template.defaultfilters import slugify
from taggit.models import Tag
from django.shortcuts import get_object_or_404
# Create your views here.

def video(request):
    if request.method == 'POST':
        url = request.POST.get('link')
        
        d = Item.objects.filter(video=url)
        if d.exists() or url is None:
            pass
        else:
            s = Item(video = url)
            s.save()

    obj = Item.objects.all()
    return render(request,'video.html',{'obj':obj})

def DeviceUpload(request):
    videofiles = DeviceVideo.objects.order_by('title')
    # Show most common tags
    common_tags = DeviceVideo.tags.most_common()[:4]
    form = DeviceVideoForm(request.POST,request.FILES)
    if form.is_valid():
        newvideo = form.save(commit=False)
        newvideo.slug = slugify(newvideo.title)
        newvideo.save()
        form.save_m2m()

    context = {
        'videos':videofiles,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request,'device.html',context)


def tagged(request,slug):
    tag = get_object_or_404(Tag,slug = slug)
    # Filter posts by tag name
    video = DeviceVideo.objects.filter(tags = tag)
    context = {
        'tag':tag,
        'videos':video,
    }

    return render(request,'device.html',context)


def detail_view(request, slug):
    video = get_object_or_404(DeviceVideo, slug=slug)
    context = {
        'video':video,
    }
    return render(request, 'detail.html', context)



def youtube_search(request):
    if request.method == 'POST':
        video_url=request.POST['video_url']
        # video_url = 'https://www.youtube.com/watch?v=LIlmQ8xhRRI'
        yt = YouTube(video_url)
        thumbnail_url = yt.thumbnail_url
        title = yt.title
        desc = yt.description
        # youtube = YTvideos(title=title,description=desc,thumbnail_url=thumbnail_url, slug = slugify(title))
        res = render(request,'youtube.html',{"title":title,"thumbnail_url":thumbnail_url,"video_url":video_url})
        return res
    else:
        return render(request,'youtube.html')


def youtube_down(request):
	if request.method == 'POST':
		formatRadio = request.POST.get('formatRadio')
		if formatRadio != "audio":
			qualityRadio = request.POST.get('qualityRadio')
		video_url_d = request.POST.get('video_url_d')
		print(formatRadio)
		# print(qualityRadio)
		yt = YouTube(str(video_url_d))
		print(yt)
		print("Downloading start ....")
		if formatRadio == "audio":
			yt.streams.filter(type = formatRadio).last().download(settings.MEDIA_ROOT)
		else:
			yt.streams.filter(type = formatRadio,resolution=qualityRadio).first().download(settings.MEDIA_ROOT)
		print("Downloding completed")
	return render(request,'youtube.html',{"msg":"downloading completed"})