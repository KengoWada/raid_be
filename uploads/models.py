import json

from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

User = get_user_model()


class XrayUpload(models.Model):
    uuid = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=False, blank=False)
    images = ArrayField(models.URLField())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'xray_uploads'
        verbose_name = 'X-Ray Uploads'
        verbose_name_plural = 'X-Ray Uploads'


class UploadResult(models.Model):
    xray_upload = models.ForeignKey(XrayUpload, on_delete=models.CASCADE)
    image = models.URLField(blank=True)
    results = models.TextField()
    result_image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'xray_uploads_results'
        verbose_name = 'X-Ray Uploads Results'
        verbose_name_plural = 'X-Ray Uploads Results'

    @property
    def uploadResults(self):
        return json.loads(self.results)
