from django.urls import path
from . import views

urlpatterns = [
    path("video", views.video, name="video"),
    path("newvideo/",views.new_video, name="newvideo"),
]