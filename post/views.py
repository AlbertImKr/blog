from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import View

from .forms import PostCreateForm
from .models import Category
from .models import Post


class HomeView(View):
    template_name = 'post/index.html'

    def get(self, request, *args, **kwargs):
        latest_posts = Post.objects.all().order_by('-created_at')[:10]
        top_viewed_posts = Post.objects.all().order_by('-created_at')[:3]
        most_popular_posts = Post.objects.all().order_by('-created_at')[:4]

        # 컨텍스트 데이터
        context = {
            'latest_posts': latest_posts,
            'top_viewed_posts': top_viewed_posts,
            'most_popular_post': most_popular_posts[0],
            'second_most_popular_post': most_popular_posts[1],
            'third_most_popular_post': most_popular_posts[2],
            'fourth_most_popular_post': most_popular_posts[3],
        }

        # 렌더링 및 응답 반환
        return render(request, self.template_name, context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('signin')

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
        categories = Category.objects.filter(posts__author=author).annotate(
                post_count=Count('posts')).order_by('-post_count')[:5]
        context['categories'] = categories
        return context
