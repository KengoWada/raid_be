from rest_framework import serializers

from .models import XrayUpload, UploadResult


class XrayUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = XrayUpload
        read_only_fields = ('created_at', 'updated_at')
        fields = ('id', 'uuid', 'description',
                  'images', 'created_at', 'updated_at')

        user = serializers.ReadOnlyField()


class CreateUploadResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadResult
        fields = ('id', 'image', 'results', 'result_image')

        xray_upload = serializers.ReadOnlyField()


class UploadResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadResult
        fields = ('id', 'image', 'results', 'result_image',
                  'created_at', 'updated_at')

        results = serializers.SerializerMethodField('get_upload_results')

    def get_upload_results(self, obj):
        return obj.uploadResults
