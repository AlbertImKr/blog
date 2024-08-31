from django.db.models import Count
from django.db.models import Q

from .models import Post


def create_post_search_criteria(keywords):
    """
    주어진 검색어를 바탕으로 Post 모델에 대한 필터링 조건을 생성합니다.
    검색어 구분자: 쉼표
    타이틀 검색: 기본 검색어
    유저이름 검색: @으로 시작
    카테고리 검색: !으로 시작
    태그 검색: #으로 시작

    :param keywords: 검색어 리스트
    :return: 필터링 조건을 나타내는 Q 객체
    """
    filter_criteria = Q()
    for keyword in keywords:
        if keyword.startswith("@"):
            filter_criteria &= Q(author__username=keyword[1:])
        elif keyword.startswith("!"):
            filter_criteria &= Q(category__name=keyword[1:])
        elif keyword.startswith("#"):
            filter_criteria &= Q(tags__name=keyword[1:])
        else:
            filter_criteria &= Q(title__icontains=keyword)
    return filter_criteria


def get_trending_posts(quantity=4):
    """
    조회수가 높은 포스트를 반환합니다.

    :param quantity: 조회수가 높은 포스트의 개수 (기본값: 4)
    :return: 조회수가 높은 포스트 리스트
    """
    return Post.objects.order_by("-created_at")[:quantity]


def get_trending_categories(quantity=5):
    """
    가장 인기 있는 카테고리를 조회합니다.

    :param quantity: 인기 있는 카테고리의 개수 (기본값: 5)
    :return: 인기 있는 카테고리 리스트
    """
    trending_categories = (
        Post.objects.values("category__name")
        .annotate(post_count=Count("category"))
        .order_by("-post_count")[:quantity]
    )
    return [item["category__name"] for item in trending_categories]


def get_trending_tags(quantity=5):
    """
    가장 인기 있는 태그를 조회합니다.

    :param quantity: 인기 있는 태그의 개수 (기본값: 5)
    :return: 인기 있는 태그 리스트
    """
    trending_tags = (
        Post.objects.values("tags__name")
        .annotate(post_count=Count("tags"))
        .filter(post_count__gte=1)
        .order_by("-post_count")[:quantity]
    )
    return [item["tags__name"] for item in trending_tags]


def get_author_most_categories(author, quantity=5):
    """
    주어진 작가가 가장 많이 작성한 카테고리를 조회합니다.

    :param author: User 인스턴스, 작가
    :param quantity: 작가가 가장 많이 작성한 카테고리의 개수 (기본값: 5)
    :return: [{'name': '카테고리 이름', 'post_count': '게시물 개수'}, ...] 형태의 리스트
    """
    categories = (
        Post.objects.filter(author=author)
        .values("category__name")
        .annotate(post_count=Count("category"))
        .order_by("-post_count")[:quantity]
    )
    return [{"name": item["category__name"], "post_count": item["post_count"]}
            for item in categories]


def get_recent_posts(quantity=5):
    """
    최근 작성된 포스트를 조회합니다.

    :param quantity: 최근 작성된 포스트의 개수 (기본값: 5)
    :return: 최근 작성된 포스트 리스트
    """
    return Post.objects.order_by("-created_at")[:quantity]


class PostSearchMixin:
    """
    검색 기능을 제공하는 뷰에 상속할 Mixin 클래스입니다.
    """

    def get_queryset(self):
        """
        검색어를 바탕으로 필터링된 Post 쿼리셋을 반환합니다.


        :return: 필터링된 Post 쿼리셋
        """
        keywords = self.get_keywords()
        filter_criteria = create_post_search_criteria(keywords)
        return Post.objects.filter(filter_criteria).order_by("-created_at")

    def get_context_data(self, **kwargs):
        """
        검색어, 인기 있는 카테고리, 인기 있는 포스트를 context에 추가합니다.
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "keywords": self.get_keywords(),
                "trending_categories": get_trending_categories(),
                "trending_posts": get_trending_posts(),
            }
        )
        return context

    def get_keywords(self):
        """
        GET 요청으로부터 keyword 파라미터를 추출하여 검색어 리스트를 반환합니다.

        :return: 검색어 리스트
        """
        keywords = self.request.GET.get("keyword", "")
        return [keyword.strip() for keyword in keywords.split(",")
                if keyword.strip()]
