from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login, logout


class User(AbstractUser):
    cellphone = models.CharField(max_length=15, unique=True)
    organization_name = models.CharField(max_length=15)
    educational_interface_name = models.CharField(max_length=200)
    description = models.TextField()
    date_of_establishment = models.DateField(null=True)
    extra = models.JSONField(default=dict)

    def login(self, request):
        if self.is_active:
            login(request, self)

    def logout(self, request):
        if self.is_active:
            logout(request)
