from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import uploads_crud


class CreateFetchXrayUploadsAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        return uploads_crud.create(request)

    def get(self, request):
        return uploads_crud.get(request)
