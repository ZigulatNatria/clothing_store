from django.db import models
from shop.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    DELIVERY = [
        ('Почтой России', 'Почтой России'),
        ('Транспортной компанией', 'Транспортной компанией'),
        ('Самовывоз', 'Самовывоз'),
    ]

    authorUser = models.ForeignKey(User, verbose_name='клиент', on_delete=models.CASCADE, null=True)
    name = models.CharField(verbose_name='ФИО', max_length=250)
    country = models.CharField(verbose_name='страна', max_length=100, null=True)
    # last_name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='эл.почта')
    address = models.CharField(verbose_name='адрес', max_length=350)
    postal_code = models.CharField(verbose_name='индекс', max_length=20)
    city = models.CharField(verbose_name='город', max_length=100)
    phone = models.IntegerField(verbose_name='номер телефона', null=True) #TODO переделать на PhoneNumberField
    delivery = models.CharField(verbose_name='способ доставки', max_length=100, choices=DELIVERY, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Заказ № {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_absolute_url(self):
        return f'/orders/order_list/'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    user = models.CharField(max_length=250, null=True)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    color = models.CharField(max_length=250, null=True)
    size = models.CharField(max_length=250, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
