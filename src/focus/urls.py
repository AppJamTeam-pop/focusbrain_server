from django.urls import path

from focus.views import FocusView


urlpatterns = [
    path('', FocusView.as_view())
]