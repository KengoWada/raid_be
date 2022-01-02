from django.urls import path

from .views import (CreateFetchXrayUploadsAPIView,
                    FetchUpdateDeleteXrayUploadsAPIView,
                    FetchXrayUploadResultsAPIView)

urlpatterns = [
    path('', CreateFetchXrayUploadsAPIView.as_view()),
    path('<int:upload_id>/', FetchUpdateDeleteXrayUploadsAPIView.as_view()),
    path('<int:upload_id>/results/', FetchXrayUploadResultsAPIView.as_view()),
]
