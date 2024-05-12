from django import forms

from .models import Remember
from .widget import CustomOpenLayersWidget


class RememberForm(forms.ModelForm):
    """
    Сustom form with custom widget for selecting a location on the map
    """

    class Meta:
        model = Remember
        fields = ["title", "comment", "location"]
        labels = {
            "title": "Название",
            "comment": "Комментарий",
            "location": "Локация",
        }
        widgets = {
            "location": CustomOpenLayersWidget(),
        }
