from django.urls import path
from . import views

urlpatterns = [
    path("links/", views.links, name="links"),
    path("new_link/",views.new_link, name="new_link"),
]