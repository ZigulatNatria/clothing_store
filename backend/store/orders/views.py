from django.shortcuts import render
from django.views.generic import ListView, UpdateView
import uuid
from django.http import HttpResponseRedirect

from .models import OrderItem, Order
from .forms import OrderCreateForm, OrderUpdateForm
from cart.cart import Cart
from yookassa import Configuration, Payment

Configuration.account_id = '232354'
Configuration.secret_key = 'test_00aCox20214_yPcvdR8-Gc79fpbkgMyh0ZgdVxH5Y1Y'



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity']
                                         )

            total = cart.get_total_price()
            print(order)
            payment = Payment.create({
                "amount": {
                    "value": f'{total}',
                    "currency": "RUB",
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": "http://127.0.0.1:8000/"
                },
                "capture": True,
                "description": f'{order}'
            }, uuid.uuid4())
            # очистить корзину
            cart.clear()
            return HttpResponseRedirect(payment.confirmation.confirmation_url)

            # return render(request,
            #               'orders/pay.html',
            #               {'order': order,
            #                'cart': cart,
            #                }
            #               )
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/create.html',
                  {'cart': cart, 'form': form}
                  )


class OrderList(ListView):
    model = OrderItem
    context_object_name = 'orders'
    template_name = 'orders/order_list.html'
    queryset = OrderItem.objects.all()


class OrderUpdate(UpdateView):
    template_name = 'orders/create.html'
    form_class = OrderUpdateForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Order.objects.get(pk=id)

