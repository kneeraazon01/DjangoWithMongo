from django.urls import path
from .views import ordersCreateView

urlpatterns = [
    path("", ordersCreateView.as_view(), name="orders"),
    # path("orders/", orderListView.as_view(), name="orderss"),
]
