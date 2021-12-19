from rest_framework import serializers

from .models import XrayUpload


class XrayUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = XrayUpload
        read_only_fields = ('created_at', 'updated_at')
        fields = ('id', 'uuid', 'description',
                  'images', 'created_at', 'updated_at')

        user = serializers.ReadOnlyField()
