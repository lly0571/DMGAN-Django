from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve
from . import views


app_name = 'ImageGeneration'
#appname & media
urlpatterns = [
    # two paths: with or without given image
    path('', views.index, name='index'),
    re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
