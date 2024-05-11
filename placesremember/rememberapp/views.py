from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import Form
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import RememberForm
from .models import Remember


class RememberListView(LoginRequiredMixin, ListView):
    queryset = Remember.objects.all()
    context_object_name = "remembers"
    template_name = "rememberapp/list_of_remembers.html"


@login_required
def add_remember(request: HttpRequest) -> HttpResponse:
    return render(request, "rememberapp/add_new_remember.html", {})


class RememberCreateView(LoginRequiredMixin, CreateView):
    model = Remember
    success_url = reverse_lazy("remember-list")

    def get_form_class(self) -> type[RememberForm]:
        return RememberForm

    def form_valid(self, form: Form) -> HttpResponse:
        print(form.instance.location)
        form.instance.user = self.request.user
        return super(RememberCreateView, self).form_valid(form)
