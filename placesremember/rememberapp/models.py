from django.contrib.auth import get_user_model
from django.contrib.gis.db import models
from django.urls import reverse

User = get_user_model()


class Remember(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    comment = models.TextField()
    created = models.DateField(auto_now_add=True)
    location = models.PointField()

    class Meta:
        indexes = [
            models.Index(fields=["-created"]),
        ]
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("remember-update", args=[self.id])
