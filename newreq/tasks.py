from __future__ import absolute_import
import requests
from .models import Call
from celery import shared_task


@shared_task
def update_model(url, instance_id):
    instance = Call.objects.get(pk=instance_id)
    try:
        r = requests.get(url)
        response = r.status_code
        instance.response = response
    except:
        instance.response = 'No response received.'
    instance.processed = True
    instance.save()