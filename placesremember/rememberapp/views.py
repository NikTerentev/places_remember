from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


@login_required
def remember_list(request: HttpRequest) -> HttpResponse:
    return render(request, "rememberapp/list_of_remembers.html", {})


@login_required
def add_remember(request: HttpRequest) -> HttpResponse:
    return render(request, "rememberapp/add_new_remember.html", {})
