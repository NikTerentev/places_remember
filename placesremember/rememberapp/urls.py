from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    RememberCreateView,
    RememberDeleteView,
    RememberListView,
    RememberUpdateView,
)

urlpatterns = [
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("", RememberListView.as_view(), name="remember-list"),
    path(
        "add-new-remember",
        RememberCreateView.as_view(),
        name="add-new-remember",
    ),
    path("<int:pk>", RememberUpdateView.as_view(), name="remember-update"),
    path(
        "<int:pk>/delete/",
        RememberDeleteView.as_view(),
        name="remember-delete",
    ),
]
