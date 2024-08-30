from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
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


class HomeView(ListView):
    model = Post
    template_name = "post/index.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-created_at"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all().order_by("-created_at")
        trending_categories = (
            posts.values("category__name")
            .annotate(post_count=Count("category"))
            .order_by("-post_count")[:5]
        )
        trending_categories_name = [item["category__name"] for item
                                    in trending_categories]
        trending_tags = (
            posts.values("tags__name")
            .annotate(post_count=Count("tags"))
            .filter(post_count__gte=1)
            .order_by("-post_count")[:30]
        )
        trending_tags_name = [item["tags__name"] for item in trending_tags]
        context.update({
            "top_viewed_posts": posts[:3],
            "most_popular_posts": posts[:4],
            "trending_categories": trending_categories_name,
            "trending_tags": trending_tags_name,
        })
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

        # 이 유저의 카테고리 목록에서 포스트가 제일 많은 카테고리 5개를 가져옴
        post = self.get_object()
        author = post.author
        categories = (
            Category.objects.filter(posts__author=author)
            .annotate(post_count=Count("posts"))
            .order_by("-post_count")[:5]
        )
        context["categories"] = categories
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = "post/post_update_form.html"
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("signin")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionError("수정 권한이 없습니다.")
        return obj


class PostListView(ListView):
    model = Post
    template_name = "post/post_list.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-created_at"]

    def get_queryset(self):
        queryset = Post.objects.all()

        if "username" in self.request.GET:
            user_name = self.request.GET["username"]
            queryset = queryset.filter(author__username=user_name)
        if "category" in self.request.GET:
            category = self.request.GET["category"]
            queryset = queryset.filter(category__name=category)
        if "tag" in self.request.GET:
            tag = self.request.GET["tag"]
            queryset = queryset.filter(tags__name=tag)

        return queryset.order_by(*self.ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 최근 카테고리와 최근 포스트 계산
        recent_categories = (
            self.get_queryset()
            .values("category__name")
            .annotate(post_count=Count("category"))
            .order_by("-post_count")[:5]
        )
        context["recent_categories"] = [
            item["category__name"] for item in recent_categories
        ]
        context["recent_posts"] = self.get_queryset().order_by("-created_at")[:5]

        keywords = []
        # 추가적인 컨텍스트 설정
        if "username" in self.request.GET:
            keywords.append(f"@{self.request.GET['username']}")
        if "category" in self.request.GET:
            keywords.append(f"!{self.request.GET['category']}")
        if "tag" in self.request.GET:
            keywords.append(f"#{self.request.GET['tag']}")
        if keywords:
            context["keywords"] = keywords
        else:
            context["keywords"] = []
        return context


class PostListFragmentView(ListView):
    model = Post
    template_name = "post/post_list_fragment.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-created_at"]

    def get_queryset(self):
        queryset = Post.objects.all()

        if "username" in self.request.GET:
            user_name = self.request.GET["username"]
            queryset = queryset.filter(author__username=user_name)
        if "category" in self.request.GET:
            category = self.request.GET["category"]
            queryset = queryset.filter(category__name=category)
        if "tag" in self.request.GET:
            tag = self.request.GET["tag"]
            queryset = queryset.filter(tags__name=tag)

        return queryset.order_by(*self.ordering)


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
