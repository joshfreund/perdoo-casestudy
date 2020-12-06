from django.db import models


class Call(models.Model):
    user = models.CharField(max_length=255)
    req_date = models.CharField(max_length=255)
    url = models.TextField()
    processed = models.BooleanField(default=False)
    response = models.TextField(blank=True)