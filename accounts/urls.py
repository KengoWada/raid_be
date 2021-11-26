from django.urls import path

from .views import UserCreateAPIView, UserRetrieveUpdateDeleteAPIView


urlpatterns = [
    path('user/', UserRetrieveUpdateDeleteAPIView.as_view()),
    path('register/', UserCreateAPIView.as_view()),
]
