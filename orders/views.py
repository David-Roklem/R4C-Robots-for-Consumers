from django.shortcuts import render
from orders.forms import OrderForm
from orders.models import Order
from customers.models import Customer
from django.core.mail import send_mail
from R4C.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


def new_order(request):
    if request.method == 'POST':
        data = request.POST
        if data:
            email = data.get('email')
            serial = f'{data.get("model")}-{data.get("version")}'.upper()
            customer = Customer(email=email)
            customer.save()
            order = Order(
                customer=customer,
                robot_serial=serial
            )
            order.save()
            send_mail(
                'Order',
                'An order has been made',
                DEFAULT_FROM_EMAIL,
                RECIPIENTS_EMAIL
            )
            return render(request, 'success.html')
    else:
        form = OrderForm()
        return render(request, 'order.html', {'form': form})
