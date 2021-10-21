from django.contrib import admin
from django.urls import path, include
from .views import LandingPage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LandingPage, name="landingpage"),
    path("registeration/", include("registeration.urls")),
    path("create_orders/", include("createOrders.urls")),
]
