from typing import Any, Optional

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    User profile model, stores a link to the avatar
    """

    user: User = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    avatar: Optional[str] = models.CharField(
        max_length=1000, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"Профиль {self.user.username}"

    def save(self, *args: Any, **kwargs: Any) -> None:
        super(Profile, self).save(*args, **kwargs)
