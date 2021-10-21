from django.shortcuts import render, redirect
from .models import CreateOrderModel

# Create your views here.
def createOrdersView(request):
    if request.method == "POST":
        patient = request.POST.get("patient")
        medicine = request.POST.get("medicine")

        order = CreateOrderModel.object.create(patient=patient, medicine=medicine)
        order.save()
        return redirect("create_orders")
    else:
        return render(request, "createOrders/create_orders.html")
