from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import PostCreateForm
from .models import Category
from .models import Post
from .services import PostSearchMixin
from .services import get_author_most_categories
from .services import get_trending_categories
from .services import get_trending_posts
from .services import get_trending_tags


class HomeView(ListView):
    model = Post
    template_name = "post/index.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-created_at"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
                {
                    "top_viewed_posts": get_trending_posts(),
                    "trending_categories": get_trending_categories(),
                    "trending_tags": get_trending_tags()
                }
        )
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("signin")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context["categories"] = get_author_most_categories(post.author)
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = "post/post_update_form.html"
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("signin")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostListView(PostSearchMixin,ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-created_at"]


class PostListFragmentView(PostSearchMixin, ListView):
    model = Post
    template_name = "post/post_list_fragment.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-created_at"]


class PostListFragmentGridView(ListView):
    model = Post
    template_name = "post/post_list_fragment_grid.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-created_at"]


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user == post.author:
        post.delete()
        return JsonResponse(
                {"status": "성공", "message": "삭제되었습니다."}, status=204
        )
    return JsonResponse(
            {"status": "실패", "message": "삭제 권한이 없습니다."}, status=403
    )


class CategoryListView(ListView):
    model = Category
    context_object_name = "categories"
    paginate_by = 50
    ordering = ["name"]
