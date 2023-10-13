from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView
import uuid
from django.http import HttpResponseRedirect

from shop.models import ClothingCategories
from .models import OrderItem, Order
from .forms import OrderCreateForm, OrderUpdateForm
from cart.cart import Cart
from yookassa import Configuration, Payment

Configuration.account_id = '232354'
Configuration.secret_key = 'test_00aCox20214_yPcvdR8-Gc79fpbkgMyh0ZgdVxH5Y1Y'


def order_create(request):
    clothing = ClothingCategories.objects.all()
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            try:
                order.authorUser = request.user
            except Exception:
                order.authorUser = None
            order.save()

            current_user = order.authorUser
            if current_user == None:
                current_user = 'Незарегистрирован'
            else:
                current_user = order.authorUser.username
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         color=item['product'].colors,      #Берём продукт и обращаемся к полю его цвета
                                         size=item['size'],
                                         user=current_user
                                         )

            total = cart.get_total_price()
            print(f'http://127.0.0.1:8000/orders/order_detail/{order.id}/')
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
                "description": f'http://127.0.0.1:8000/orders/order_detail/{order.id}/'
            }, uuid.uuid4())
            # очистить корзину
            cart.clear()
            return HttpResponseRedirect(payment.confirmation.confirmation_url)

    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/create.html',
                  {'cart': cart, 'form': form, 'clothing': clothing}
                  )


class OrderList(ListView):
    model = OrderItem
    context_object_name = 'orders'
    template_name = 'orders/order_list.html'
    queryset = OrderItem.objects.all()


class OrderUpdate(UpdateView):
    template_name = 'orders/update.html'
    form_class = OrderUpdateForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Order.objects.get(pk=id)


class OrderDetail(DetailView):
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'
    queryset = Order.objects.all()

    def all_items_order(self):
        current_order = self.get_object()
        items = OrderItem.objects.filter(order=current_order.id)
        return items


