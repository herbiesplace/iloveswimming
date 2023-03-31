from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from main.decorators import user_is_superuser
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from .models import Video, Analyse
from .forms import VideoForm
from django.contrib import messages

@login_required
def video(request):
    videos = Video.objects.all()
    analyses = Analyse.objects.all()
    return render(request, 'video/video.html' , {"videos":videos,"analyses":analyses})
 
@login_required
def new_video(request):
     
    if request.method=="POST":
        form=VideoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
             
            messages.success(request, "Video is succesvol opgeladen, bedankt, u krijgt een melding als de analyse klaar is.")
            return redirect("video")
    else:
        form=VideoForm()
    return render(request,'video/new_video.html', {"form":form})