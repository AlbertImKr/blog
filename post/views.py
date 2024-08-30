from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import View

from .forms import PostCreateForm
from .models import Category
from .models import Post


class HomeView(View):
    template_name = "post/index.html"

    def get(self, request, *args, **kwargs):
        latest_posts = Post.objects.all().order_by("-created_at")[:10]
        top_viewed_posts = Post.objects.all().order_by("-created_at")[:3]
        most_popular_posts = Post.objects.all().order_by("-created_at")[:4]

        # 컨텍스트 데이터
        context = {
            "latest_posts": latest_posts,
            "top_viewed_posts": top_viewed_posts,
            "most_popular_post": most_popular_posts[0],
            "second_most_popular_post": most_popular_posts[1],
            "third_most_popular_post": most_popular_posts[2],
            "fourth_most_popular_post": most_popular_posts[3],
        }

        # 렌더링 및 응답 반환
        return render(request, self.template_name, context)


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


class PostListPartialView(ListView):
    model = Post
    template_name = "post/post_list_partial.html"
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
