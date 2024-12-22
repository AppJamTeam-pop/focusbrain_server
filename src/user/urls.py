from django.urls import path

from user.views import MyUserInfoView

urlpatterns = [
    path('', MyUserInfoView.as_view())
]