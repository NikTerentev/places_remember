from django.contrib.auth import views as auth_views
from django.urls import path

from .views import add_remember, remember_list

urlpatterns = [
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("remembers/", remember_list, name="remember-list"),
    path("add-new-remember/", add_remember, name="add-new-remember"),
]
