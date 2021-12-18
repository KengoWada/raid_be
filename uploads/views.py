from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import uploads_crud
from .docs import request_body, responses


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
