from django.urls import path, include

app_name = 'video'

urlpatterns = [
    path('video/', include('video.views.videos.urls'))
]
