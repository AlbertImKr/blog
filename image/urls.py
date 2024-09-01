from django.urls import path

from .views import GeneratePresignedUrlView
from .views import UploadImageView

urlpatterns = [
    path("api/generate-presigned-url/", GeneratePresignedUrlView.as_view(),
         name="generate_presigned_url"),
    path("api/upload-image/", UploadImageView.as_view(), name="upload_image"),
]
