import os
from typing import Any, Optional

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help: str = "Add admin"

    def handle(self, *args: Any, **options: Any) -> None:
        username: Optional[str] = os.getenv("ADMIN_USER")
        password: Optional[str] = os.getenv("ADMIN_PASSWORD")

        user: Optional[AbstractUser] = (
            get_user_model().objects.filter(username=username).first()
        )
        if not user:
            get_user_model().objects.create_superuser(
                username=username, password=password, email="admin@mail.ru"
            )
