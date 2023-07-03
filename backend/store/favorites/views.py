from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .favorites import Favorites
from .forms import FavoritesAddProductForm


@require_POST
def favorites_add(request, product_id):
    cart = Favorites(request)
    product = get_object_or_404(Product, id=product_id)
    form = FavoritesAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 update_quantity=cd['update']
                 )
    return redirect('favorites_detail')


def favorites_remove(request, product_id):
    cart = Favorites(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('favorites_detail')


def favorites_detail(request):
    cart = Favorites(request)
    return render(request, 'favorites/detail.html', {'cart': cart})

