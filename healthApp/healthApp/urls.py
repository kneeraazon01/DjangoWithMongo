from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView, name="home"),
    path("registeration/", include("registeration.urls")),
    path("create_orders/", include("createOrders.urls")),
]
