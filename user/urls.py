from django.urls import path

from .views import SignInView
from .views import SignOutView
from .views import SignupView
from .views import UserManageView
from .views import UserPostListFragmentView
from .views import UserPostListView
from .views import UserProfileUpdateView
from .views import UserPasswordChangeView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', SignOutView.as_view(), name='signout'),
    path('users/posts/', UserPostListView.as_view(), name='user_posts'),
    path('users/manage/', UserManageView.as_view(), name='user_manage'),
    path('users/posts/fragment/', UserPostListFragmentView.as_view(),
         name='user_posts_partial'),
    path('users/profile/', UserProfileUpdateView.as_view(),
         name='user_profile_edit'),
    path('users/password/', UserPasswordChangeView.as_view(),
         name='user_password_edit'),
]
