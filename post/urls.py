from django.urls import path

from .views import CategoryListView
from .views import HomeView
from .views import PostCreateView
from .views import PostDeleteView
from .views import PostDetailView
from .views import PostListFragmentGridView
from .views import PostListFragmentView
from .views import PostListView
from .views import PostUpdateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("posts/new", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/fragment/", PostListFragmentView.as_view(),
         name="post_list_partial"),
    path("posts/fragment/grid/", PostListFragmentGridView.as_view()
         , name="post_list_partial_grid"),
    path("categories/",CategoryListView.as_view(),name="category_list"),
]
