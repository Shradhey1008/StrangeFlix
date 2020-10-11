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

    lastvideo= Video.objects.last()

    videofile = lastvideo.videofile


    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

        
    context= {'videofile': videofile,
            'form': form
            }
    # context= {
    #         'form': form
    #         }
        
        
    return render(request, 'upload.html',context)