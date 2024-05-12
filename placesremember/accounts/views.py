from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View


class HelloPageView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect("/remembers")
        return render(request, "accounts/hello_page.html", {})
