from django.urls import path

from .views import HelloPageView

urlpatterns = [path("", HelloPageView.as_view(), name="hello-page")]
