from django.shortcuts import render

from .models import OrderItem
from .forms import CustomerOrderForm
from cart.cart import Cart

def create_order_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CustomerOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(customer=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            cart.clear()
            return render(request, 'order_complete.html', {'order':order})
    form = CustomerOrderForm()
    return render(request, 'order.html', {'cart':cart, 'form':form})