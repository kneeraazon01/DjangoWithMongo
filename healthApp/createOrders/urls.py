from django.urls import path
from .views import createOrdersView

urlpatterns = [
    path("", createOrdersView, name="register"),
]
