from django.urls import path

from .views import SignInView
from .views import SignOutView
from .views import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', SignOutView.as_view(), name='signout'),
]
