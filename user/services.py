from post.services import create_post_search_criteria


class UserPostsSearchMixin:
    """
    유저의 게시글을 검색하는 기능을 제공하는 Mixin 클래스입니다.
    """
    context_object_name = "posts"
    paginate_by = 10
    ordering = "-created_at"

    def get_queryset(self):
        """
        검색어를 바탕으로 필터링된 유저의 게시글 퀴리셋을 반환합니다.
        """
        user = self.request.user
        keywords = self._get_keywords()
        filter_criteria = create_post_search_criteria(keywords)
        ordering = self.request.GET.getlist("ordering", self.ordering)
        return user.posts.filter(filter_criteria).order_by(ordering)

    def get_context_data(self, **kwargs):
        """
        게시글 총 개수를 context에 추가합니다.
        """
        context = super().get_context_data(**kwargs)
        context["total_posts"] = self.get_queryset().count()
        return context

    def _get_keywords(self):
        """
        GET 요청으로부터 keyword 파라미터를 추출하여 검색어 리스트를 반환합니다.
        """
        keywords = self.request.GET.get("keyword", "")
        return [keyword.strip() for keyword in keywords.split(",")
                if keyword.strip()]

