from django.urls import path

from .views import HomeView
from .views import PostCreateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("posts/new", PostCreateView.as_view(), name="post_create"),
]
