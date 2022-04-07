from django.shortcuts import render, redirect
from order.models import Order,OrderForm

# Create your views here.

def all_orders(request):
    order_objects = Order.objects.all()
    context = {'order_objects': order_objects}
    return render(request, 'order/all_orders.html', context)

def ordered_orders(request):
    order_objects = Order.objects.all().order_by('created_at', 'plated_end_at')
    context = {'order_objects': order_objects}
    return render(request, 'order/ordered_orders.html', context)

def filtered_orders(request):
    order_objects = Order.objects.filter(created_at__gt='end_at')
    context = {'order_objects': order_objects}
    return render(request, 'order/ordered_orders.html', context)
def add_order(request,id=0):
    if request.method == "GET":
        if id==0:
            form = OrderForm()
        else:
            order=Order.objects.get(pk=id)
            form=OrderForm(instance=order)
        submit = "Add"
        context = {'form': form,
                   'submit': submit}
        return render(request, 'order/add_order.html', context)
    else:
        if id == 0:
            form = OrderForm(request.POST)
        else:
            order=Order.objects.get(pk=id)
            form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
        return redirect('/orders/all_orders')