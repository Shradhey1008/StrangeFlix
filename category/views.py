from django.shortcuts import render, redirect
from .models import Video, Category
from subscriptions.models import UserMembership
# Create your views here.

def CategoryList(request):
    categories = Category.objects.all()
    context = {'objects':categories}
    return render(request,'category.html',context)

def CategoryView(request,slug):
    category_qs = Category.objects.filter(slug =slug)
    print(category_qs)
    if category_qs.exists():
        category = category_qs.first()
    print(category)

    videos_qs = category.videos.all()
    print(videos_qs)
    # categories = Video.objects.filter()
    context = {'objects':videos_qs}
    return render(request,'category_videos.html',context)

def Category_video(request,category_slug,categoryvideo_slug,*args, **kwargs):
    category_qs = Category.objects.filter(slug = category_slug)
    print(category_qs)
    if category_qs.exists():
        category = category_qs.first()
    print(category)

    videos_qs = category.videos.filter(slug = categoryvideo_slug)
    print(videos_qs)
    if videos_qs.exists():
        video = videos_qs.first()

    user_membership = UserMembership.objects.filter(user=request.user).first()
    user_membership_type = user_membership.membership.membership_type

    category_allowed_mem_type = category.allowed_membership.all()

    context = {'objects': None}
    if category_allowed_mem_type.filter(membership_type=user_membership_type).exists():
        context = {'objects':video}

    return render(request,'video_cat.html',context)
