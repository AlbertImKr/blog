from django.urls import path

from .views import SignupView
from .views import LoginView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
]
