from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import RegisterModel


class registerCreateView(CreateView):
    model = RegisterModel
    template_name = "registeration/register.html"
    fields = ["name", "address"]
    success_url = reverse_lazy("register")


class userListView(ListView):
    model = RegisterModel
    template_name = "registeration/users.html"
    context_object_name = "users"
