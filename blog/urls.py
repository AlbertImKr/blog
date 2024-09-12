from django.contrib import admin
from django.urls import include
from django.urls import path

from . import settings
from .views import ContactView

urlpatterns = [
    path("", include("post.urls")),
    path("", include("user.urls")),
    path("contact/", ContactView.as_view(), name="contact"),
    path("", include("image.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("admin/", admin.site.urls),
    ]
