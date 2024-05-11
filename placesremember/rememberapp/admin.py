from django.contrib.gis import admin

from .models import Remember


@admin.register(Remember)
class RememberAdmin(admin.GISModelAdmin):
    list_display = ("user", "title", "comment", "created", "location")
