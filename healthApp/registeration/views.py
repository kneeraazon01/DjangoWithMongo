from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import RegisterModel


# Create your views here.
def RegisterView(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")

        user = User.objects.create_user(name=name, address=address)
        user.save()
        messages.success(request, "Registered!")
        return redirect("register")
    else:
        return render(request, "registeration/register.html")
