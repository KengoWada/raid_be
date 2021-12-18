from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import uploads_crud
from .docs import request_body, responses
from .models import XrayUpload
from .permissions import IsOwner


class CreateFetchXrayUploadsAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=request_body.CREATE_UPLOAD_SCHEMA,
        responses=responses.CREATE_UPLOAD_RESPONSE,
        operation_id='Add xray uploads',
        operation_description='Add xray uploads',
    )
    def post(self, request):
        return uploads_crud.create(request)

    @swagger_auto_schema(
        responses=responses.FETCH_UPLOADS_RESPONSE,
        operation_id='Fetch xray uploads',
        operation_description='Fetch xray uploads',
    )
    def get(self, request):
        return uploads_crud.get(request)


class FetchUpdateDeleteXrayUploadsAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_object(self, pk):
        try:
            xray_upload = XrayUpload.objects.get(pk=pk)
            self.check_object_permissions(self.request, xray_upload)
            return xray_upload
        except XrayUpload.DoesNotExist:
            return None

    @swagger_auto_schema(
        responses=responses.FETCH_UPLOAD_RESPONSE,
        operation_id='Fetch xray upload',
        operation_description='Fetch xray upload',
    )
    def get(self, request, upload_id):
        upload = self.get_object(upload_id)
        return uploads_crud.get_upload(upload)

    @swagger_auto_schema(
        request_body=request_body.UPDATE_UPLOAD_SCHEMA,
        responses=responses.UPDATE_UPLOAD_RESPONSE,
        operation_id='Update xray upload',
        operation_description='Update xray upload',
    )
    def patch(self, request, upload_id):
        upload = self.get_object(upload_id)
        return uploads_crud.update(upload, request)

    @swagger_auto_schema(
        responses=responses.DELETE_UPLOAD_RESPONSE,
        operation_id='Delete xray upload',
        operation_description='Delete xray upload',
    )
    def delete(self, request, upload_id):
        upload = self.get_object(upload_id)
        return uploads_crud.delete(upload)
