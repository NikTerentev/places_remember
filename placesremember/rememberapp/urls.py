from django.contrib.auth import views as auth_views
from django.urls import path

from .views import remember_list

urlpatterns = [
    path("remembers/", remember_list, name="remember-list"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
