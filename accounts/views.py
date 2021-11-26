from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import user_crud


class UserCreateAPIView(APIView):

    def post(self, request):
        return user_crud.create(request)


class UserRetrieveUpdateDeleteAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return user_crud.get(request)

    def put(self, request):
        return user_crud.update(request)

    def delete(self, request):
        return user_crud.delete(request)
