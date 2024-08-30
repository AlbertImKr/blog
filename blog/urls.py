from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import ContactView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("post.urls")),
    path("", include("user.urls")),
    path("contact/", ContactView.as_view(), name="contact"),
]
