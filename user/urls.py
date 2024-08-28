from django.urls import path

from .views import SignInView
from .views import SignOutView
from .views import SignupView
from .views import UserPostListView
from .views import UserManageView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', SignOutView.as_view(), name='signout'),
    path('users/posts/', UserPostListView.as_view(), name='user_posts'),
    path('users/manage/', UserManageView.as_view(), name='user_manage'),
]
