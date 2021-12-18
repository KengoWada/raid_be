from django.urls import path

from .views import CreateFetchXrayUploadsAPIView, FetchUpdateDeleteXrayUploadsAPIView

urlpatterns = [
    path('', CreateFetchXrayUploadsAPIView.as_view()),
    path('<int:upload_id>/', FetchUpdateDeleteXrayUploadsAPIView.as_view()),
]
