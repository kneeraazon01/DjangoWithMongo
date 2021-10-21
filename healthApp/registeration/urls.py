from django.urls import path
from .views import RegisterView

urlpatterns = [
    path("", RegisterView, name="register"),
]
