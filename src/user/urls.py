from django.urls import path

from user.views import MyInfoView


urlpatterns = [
    path('/my', MyInfoView.as_view())
]