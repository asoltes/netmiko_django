from django.conf import settings
from django.db import models
from django.utils import timezone


class Device(models.Model)
    device_name = models.CharField(max_length=200, default='')
    ip_address = models.CharField(max_length=15, default='')
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.device_name

