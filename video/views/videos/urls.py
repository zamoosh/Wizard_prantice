from django.urls import path, include
from .views import *

app_name = 'videos'

urlpatterns = [
    # views
    path('videos/', videos, name='videos'),
    path('upload/', upload, name='upload'),

    # api
    path('api/', include('video.views.videos.api.apiurls'))
]
