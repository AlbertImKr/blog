from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
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
                    "trending_tags": get_trending_tags(),
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
    success_url = reverse_lazy("user_posts")
    login_url = reverse_lazy("signin")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostListView(PostSearchMixin, ListView):
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


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("user_posts")
    login_url = reverse_lazy("signin")
    template_name = "404.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class CategoryListView(ListView):
    model = Category
    context_object_name = "categories"
    paginate_by = 50
    ordering = ["name"]
