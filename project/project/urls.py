from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('bleep.urls')),
    path("", include('video.urls')),
    path("", include('users.urls')),
    path("", include('main.urls')),
    path('tinymce/', include('tinymce.urls')),
    path("", include("allauth.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
