from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import UserSigninForm
from .forms import UserSignupForm
from .services import UserPostsSearchMixin


class SignupView(CreateView):
    form_class = UserSignupForm
    template_name = "user/signup.html"
    success_url = reverse_lazy("home")

    def form_invalid(self, form):
        for _field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)


class SignInView(LoginView):
    form_class = UserSigninForm
    template_name = "user/signin.html"
    success_url = reverse_lazy("home")

    def form_invalid(self, form):
        messages.error(self.request, "아이디 또는 비밀번호가 일치하지 않습니다.")
        return super().form_invalid(form)

    def get_redirect_url(self):
        return self.request.GET.get("next", self.success_url)


class SignOutView(LogoutView):
    next_page = reverse_lazy("home")


class UserPostListView(LoginRequiredMixin, UserPostsSearchMixin, ListView):
    template_name = "user/posts.html"
    login_url = reverse_lazy("signin")


class UserPostListFragmentView(LoginRequiredMixin, UserPostsSearchMixin,
                               ListView):
    template_name = "user/post_list_fragment.html"
    login_url = reverse_lazy("signin")


class UserManageView(LoginRequiredMixin, UserPostsSearchMixin, ListView):
    template_name = "user/manage.html"
