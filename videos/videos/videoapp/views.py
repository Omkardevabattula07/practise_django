from django.shortcuts import render, redirect
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videos.html', {'videos': videos})