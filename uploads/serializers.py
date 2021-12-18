from rest_framework import serializers

from .models import XrayUpload


class XrayUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = XrayUpload
        fields = ('id', 'uuid', 'description', 'images')

    user = serializers.ReadOnlyField()
