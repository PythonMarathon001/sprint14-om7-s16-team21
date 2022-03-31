from django.shortcuts import render
from order.models import Order

# Create your views here.

def all_orders(request):
    order_objects = Order.objects.all()
    context = {'order_objects': order_objects}
    return render(request, 'order/all_orders.html', context)