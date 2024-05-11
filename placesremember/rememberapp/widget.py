from django.contrib.gis.forms.widgets import OpenLayersWidget


class CustomOpenLayersWidget(OpenLayersWidget):
    template_name = "rememberapp/custom_openlayers.html"
