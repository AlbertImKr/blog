from django.urls import path

from .views import HomeView
from .views import PostCreateView
from .views import PostDetailView
from .views import PostUpdateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("posts/new", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit", PostUpdateView.as_view(), name="post_update"),
]
