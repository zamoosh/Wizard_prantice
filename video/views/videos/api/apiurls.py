from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('chunk_upload/', chunk_upload, name='chunk_upload')
]
