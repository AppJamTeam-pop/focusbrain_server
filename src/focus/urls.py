from django.urls import path

from focus.views import FocusView, FocusRankView, MyFocusRankView

urlpatterns = [
    path('', FocusView.as_view()),
    path('/rank', FocusRankView.as_view()),
    path('/rank/my', MyFocusRankView.as_view())
]