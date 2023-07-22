import uuid
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from cart.cart import Cart
from yookassa import Configuration, Payment

Configuration.account_id = '232354'
Configuration.secret_key = 'test_00aCox20214_yPcvdR8-Gc79fpbkgMyh0ZgdVxH5Y1Y'


class Pay(View):

    def get(self, request):
        cart = Cart(request)
        total = cart.get_total_price()
        payment = Payment.create({
            "amount": {
                # "value": "100.00",
                "value": f'{total}',
                "currency": "RUB",
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://www.example.com/return_url"
            },
            "capture": True,
            "description": "Заказ №1"
        }, uuid.uuid4())
        return HttpResponseRedirect(payment.confirmation.confirmation_url)