from rest_framework import status
from rest_framework.response import Response

from .models import XrayUpload
from .paginators import XrayUploadPagination
from .serializers import XrayUploadSerializer
from .validators import validate_create_xray_upload


def create(request):
    """Upload an x-ray"""
    result = validate_create_xray_upload(request.data)
    if result:
        response = {'message': 'Invalid values', 'error': result}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    serializer = XrayUploadSerializer(data=request.data)
    if not serializer.is_valid():
        response = {'message': 'Invalid values', 'error': serializer.errors}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    serializer.save(user=request.user)

    response = {'message': 'Done', 'upload': serializer.data}
    return Response(response, status=status.HTTP_201_CREATED)


def get(request):
    """Get all a users z-ray uploads"""
    uploads = XrayUpload.objects.filter(
        user__id=request.user.id).order_by('-updated_at')

    paginator = XrayUploadPagination()
    results = paginator.paginate_queryset(uploads, request=request)

    serializer = XrayUploadSerializer(results, many=True)

    response = paginator.get_paginated_response(serializer.data)
    return Response(response, status=status.HTTP_200_OK)


def update(upload):
    """Update an x-ray title or description"""


def delete(upload):
    """Delete an x-ray upload and it's related results"""
