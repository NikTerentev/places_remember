from typing import Any, Optional

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user: User = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    # profile_photo = models.ImageField(upload_to='profile_pics')
    avatar: Optional[str] = models.CharField(
        max_length=1000, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"Профиль {self.user.username}"

    def save(self, *args: Any, **kwargs: Any) -> None:
        super(Profile, self).save(*args, **kwargs)
