from django.urls import path

from authentication.views import SigninView, SignupView, LogoutView

urlpatterns = [
    path('/login', SigninView.as_view()),
    path('/signup', SignupView.as_view()),
    path('/logout', LogoutView.as_view()),
]