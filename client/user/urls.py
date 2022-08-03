from django.urls import path
from .views import *
from .api import *

app_name = 'user'

urlpatterns = [
    path('profile/', profile, name='profile'),

    path('api/profile/', api_profile, name='api_profile')
]
