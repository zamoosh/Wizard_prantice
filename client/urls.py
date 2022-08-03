from django.urls import path, include

app_name = 'client'

urlpatterns = [
    path('user/', include('client.user.urls', namespace='user'))
]
