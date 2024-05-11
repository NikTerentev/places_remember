from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import Form
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import RememberForm
from .models import Remember


class RememberListView(LoginRequiredMixin, ListView):
    queryset = Remember.objects.all()
    context_object_name = "remembers"
    template_name = "rememberapp/list_of_remembers.html"


class RememberCreateView(LoginRequiredMixin, CreateView):
    model = Remember
    success_url = reverse_lazy("remember-list")

    def get_form_class(self) -> type[RememberForm]:
        return RememberForm

    def form_valid(self, form: Form) -> HttpResponse:
        form.instance.user = self.request.user
        return super(RememberCreateView, self).form_valid(form)


class RememberUpdateView(LoginRequiredMixin, UpdateView):
    model = Remember
    fields = ["title", "comment", "location"]
    template_name = "rememberapp/update.html"
    success_url = reverse_lazy("remember-list")

    def form_valid(self, form: Form) -> HttpResponse:
        form.instance.user = self.request.user
        return super(RememberUpdateView, self).form_valid(form)


class RememberDeleteView(LoginRequiredMixin, DeleteView):
    model = Remember
    success_url = reverse_lazy("remember-list")
