from django.contrib.auth import views as auth_views
from django.urls import path

from .views import RememberCreateView, RememberListView

urlpatterns = [
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("remembers/", RememberListView.as_view(), name="remember-list"),
    path(
        "remembers/add-new-remember/",
        RememberCreateView.as_view(),
        name="add-new-remember",
    ),
]
