import json
import time

import boto3
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from image.models import Image

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_FILE_TYPES = ["image/jpeg", "image/png", "image/jpg"]


class GeneratePresignedUrlView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        file_name = request.GET.get("file_name")
        file_type = request.GET.get("file_type")
        file_size = request.GET.get("file_size")

        if not all([file_name, file_type, file_size]):
            return JsonResponse(
                {"error": "file_name, file_type, file_size required"}, status=400
            )
        if file_size.isdigit() is False:
            return JsonResponse({"error": "file_size should be integer"}, status=400)
        if int(file_size) > MAX_FILE_SIZE:
            return JsonResponse(
                {"error": "file_size should be less than 5MB"}, status=400
            )

        if file_type not in ALLOWED_FILE_TYPES:
            return JsonResponse({"error": "file_type not allowed"}, status=400)

        s3_client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME,
        )
        file_name = f"media/{request.user.id}/{int(time.time())}_{file_name}"
        try:
            presigned_url = s3_client.generate_presigned_url(
                "put_object",
                Params={
                    "Bucket": settings.AWS_STORAGE_BUCKET_NAME,
                    "Key": file_name,
                    "ContentType": file_type,
                },
                ExpiresIn=600,
            )
            return JsonResponse({"url": presigned_url})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


class UploadImageView(LoginRequiredMixin, View):
    model = Image

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            url = data.get("url")
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        url = url.split("?")[0]
        image = Image.objects.create(user=request.user, image_url=url)
        return JsonResponse({"image_id": image.id})
