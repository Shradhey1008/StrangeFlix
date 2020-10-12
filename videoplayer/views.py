from django.shortcuts import render
from .models import Item, Video
from django.core.files.storage import FileSystemStorage
from .forms import VideoForm
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

def upload(request):

    videofiles= Video.objects.all()

    # videofile = lastvideo.videofile
    print(videofiles)

    form= VideoForm(request.POST or None, request.FILES or None)
    # print(Video.objects.filter(videofile=form.cleaned_data['videofile']).exists())
    if form.is_valid():
        if Video.objects.filter(name=request.POST.get('name')).exists():
            pass
        else:
            form.save()
        

        
    context= {'videofile': videofiles,
            'form': form
            }
    # context= {
    #         'form': form
    #         }
        
        
    return render(request, 'upload.html',context)