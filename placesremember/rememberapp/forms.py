from django import forms

from .models import Remember
from .widget import CustomOpenLayersWidget


class RememberForm(forms.ModelForm):
    class Meta:
        model = Remember
        fields = ["title", "comment", "location"]
        widgets = {
            "location": CustomOpenLayersWidget,
        }
