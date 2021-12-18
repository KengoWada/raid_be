from django.urls import path

from .views import CreateFetchXrayUploadsAPIView

urlpatterns = [
    path('', CreateFetchXrayUploadsAPIView.as_view()),
]
