from django.urls import path

from .views import hello_page

urlpatterns = [path("", hello_page, name="hello-page")]
