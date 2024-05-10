from django.conf import settings
from django.db import models


class Remember(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="remembers_created",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    comment = models.TextField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["-created"]),
        ]
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title
