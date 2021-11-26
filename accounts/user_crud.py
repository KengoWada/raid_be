from rest_framework import status
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .validators import validate_register_user, validate_update_user_details


def create(request):
    """Create a user"""
    result = validate_register_user(request.data)
    if result is not None:
        response = {'message': 'Invalid values', 'error': result}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        response = {'message': 'Invalid values', 'error': serializer.errors}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()

    response = {'message': 'Done', 'user': serializer.data}
    return Response(response, status=status.HTTP_201_CREATED)


def get(request):
    """Get a users details"""
    serializer = UserSerializer(request.user)

    response = {'message': 'Done', 'user': serializer.data}
    return Response(response, status=status.HTTP_200_OK)


def update(request):
    """Update user details"""
    result = validate_update_user_details(request.data)
    if result is not None:
        response = {'message': 'Invalid values', 'error': result}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    user = request.user.update(request.data)
    serializer = UserSerializer(user)

    response = {'message': 'Done', 'user': serializer.data}
    return Response(response, status=status.HTTP_200_OK)


def delete(request):
    """Delete a user account"""
    request.user.delete()

    response = {'message': 'Done'}
    return Response(response, status=status.HTTP_200_OK)
