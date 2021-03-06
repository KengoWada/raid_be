import json

from celery import shared_task
from decouple import config

import requests

from .models import XrayUpload
from .serializers import CreateUploadResultSerializer

AI_MODEL_API = config('AI_MODEL_API')


@shared_task
def get_xray_upload_results(pk):
    """Get xray upload results"""
    try:
        xray_upload = XrayUpload.objects.get(pk=pk)
    except XrayUpload.DoesNotExist:
        return

    data = {'images': xray_upload.images}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(AI_MODEL_API, json=data, headers=headers)
    results = response.json()
    for i in results:
        i['results'] = json.dumps(i['results'])

    serializer = CreateUploadResultSerializer(data=results, many=True)
    if not serializer.is_valid():
        return

    serializer.save(xray_upload=xray_upload)
