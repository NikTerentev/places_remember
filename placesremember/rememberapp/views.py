from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_page(request: HttpRequest) -> HttpResponse:
    return render(request, "rememberapp/hello_page.html", {})
