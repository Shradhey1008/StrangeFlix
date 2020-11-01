from django.shortcuts import render, redirect
from .models import Video, Category ,Comment
from django.urls import reverse
from subscriptions.models import UserMembership
from django.http import HttpResponseRedirect
# Create your views here.

video_obj =""

def CategoryList(request):
    categories = Category.objects.all()
    context = {'objects':categories}
    return render(request,'category.html',context)

def CategoryView(request,slug):
    category_qs = Category.objects.filter(slug=slug)
    # print(category_qs)
    if category_qs.exists():
        category = category_qs.first()
    else:
        category = None
    # print(category)
    if category:
        videos_qs = category.videos.all()
    else:
        videos_qs= None
    # print(videos_qs)
    # categories = Video.objects.filter()
    context = {'objects':videos_qs}
    return render(request,'category_videos.html',context)

def Category_video(request,category_slug,categoryvideo_slug,*args, **kwargs):
    category_qs = Category.objects.filter(slug = category_slug)
    # print(category_qs)
    if category_qs.exists():
        category = category_qs.first()
    # print(category)

    videos_qs = category.videos.filter(slug = categoryvideo_slug)
    # print(videos_qs)
    if videos_qs.exists():
        video = videos_qs.first()
        global video_obj
        video_obj =video

    user_membership = UserMembership.objects.filter(user=request.user).first()
    user_membership_type = user_membership.membership.membership_type

    category_allowed_mem_type = category.allowed_membership.all()

    context = {'objects': None,}
    if category_allowed_mem_type.filter(membership_type=user_membership_type).exists():
        context = {'objects':video}

    if request.method == "POST":
        content = request.POST.get('content')
        created_comment = Comment(post=video,user=request.user,content=content)
        created_comment.save()
    
    video_comments = Comment.objects.filter(post=video).order_by('date_posted')
    context['comments'] = video_comments


    return render(request,'video.html',context)

def videoComments(request):
    if request.method == "POST":
        global video_obj
        content = request.POST.get('content')
        created_comment = Comment(post=video_obj,user=request.user,content=content)
        created_comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
