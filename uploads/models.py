from django.contrib.postgres.fields import ArrayField
from django.db import models


class XrayUpload(models.Model):
    uuid = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=False, blank=False)
    images = ArrayField(models.URLField())
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'xray_uploads'
        verbose_name = 'X-Ray Uploads'
        verbose_name_plural = 'X-Ray Uploads'


class UploadResult(models.Model):
    pass
