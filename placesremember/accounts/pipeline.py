from typing import Any, Dict, Optional

from django.contrib.auth.models import User

from .models import Profile


def get_avatar(
    backend: Any,
    response: Dict[str, Any],
    user: Optional[User] = None,
    *args: Any,
    **kwargs: Any,
) -> None:
    """
    Function for getting a link to an avatar from a request
    """
    url = None

    if backend.name == "vk-oauth2":
        url = response.get("photo", "")
    if url:
        profile, created = Profile.objects.get_or_create(user=user)
        if created:
            profile.avatar = url
            profile.save()
