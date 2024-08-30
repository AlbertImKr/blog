from django.urls import path

from .views import HomeView
from .views import PostCreateView
from .views import PostDetailView
from .views import PostListPartialView
from .views import PostListView
from .views import PostUpdateView
from .views import delete_post

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("posts/new", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete", delete_post, name="post_delete"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/partial/", PostListPartialView.as_view(),
         name="post_list_partial"),
]
