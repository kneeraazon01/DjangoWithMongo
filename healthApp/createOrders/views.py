from typing import List
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import CreateOrderModel


class ordersCreateView(CreateView):
    model = CreateOrderModel
    template_name = "createOrders/create_orders.html"
    fields = ["patient", "medicine"]
    success_url = reverse_lazy("orders")


# class orderListView(ListView):
#     model = CreateOrderModel
#     template_name = "createOrders/orders.html"
#     context_object_name = "orders"
