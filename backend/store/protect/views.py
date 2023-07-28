from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Order, OrderItem


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def user_orders(self):
        return OrderItem.objects.filter(user=self.request.user.username)