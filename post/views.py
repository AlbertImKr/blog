from django.shortcuts import render
from django.views.generic import View

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
