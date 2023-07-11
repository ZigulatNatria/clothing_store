from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Product, CategoryProduct, ClothingCategories, Collection, News, Color, \
    Size, Favorites
from django.views.generic import ListView, DetailView, TemplateView
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# from cart.forms import CartAddProductForm
from django import forms
from django.db.models import Q
from itertools import groupby

# class ProductsListView(ListView):
#     model = Product
#     template_name = 'products_categories.html'
#     context_object_name = 'pro'
#     queryset = Product.objects.all()
#
#     def get_object(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         id = self.get(**kwargs)
#         category = CategoryProduct.objects.get(pk=id)
#         # products = Product.objects.filter(category_product=category.id)
#         context['products'] = Product.objects.filter(category_product=category.id)
#         return context


def product_categories(request, category_product_id):
    category = CategoryProduct.objects.get(pk=category_product_id)
    products = Product.objects.filter(category_product=category.id)
    clothing = ClothingCategories.objects.all()
    context = {'products': products,
               'clothing': clothing,
               }
    return render(request, 'products_categories.html', context)


class ProductDetail(DetailView):
    template_name = 'detail.html'
    context_object_name = 'product'
    queryset = Product.objects.all()

    def color(self):
        product = self.get_object()
        color_product = Color.objects.filter(vendor_code=product.vendor_code)
        return color_product

    def size(self):
        product = self.get_object()
        size_product = Size.objects.filter(vendor_code=product.vendor_code)
        return size_product

    def forma(self):

        class CartAddProductForm(forms.Form):
            PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 2)]

            colors_product = self.color()
            color_list = []
            for col in colors_product:
                color_list.append(col.name_color)

            PRODUCT_COLOR_CHOICES = [(str(k), str(k)) for k in color_list]

            size_product = self.size()
            size_list = []
            for size in size_product:
                size_list.append(size.size)

            PRODUCT_SIZE_CHOICES = [(str(s), str(s)) for s in size_list]

            quantity = forms.TypedChoiceField(label='Колличество', choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
            color = forms.TypedChoiceField(label='Цвет', choices=PRODUCT_COLOR_CHOICES, coerce=str)
            size = forms.TypedChoiceField(label='Размер', choices=PRODUCT_SIZE_CHOICES, coerce=str)
            update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
        return CartAddProductForm()

    def product_add_cart(self):
        cart_product_form = self.forma()
        return cart_product_form

    def all_product_collection(self): #Получение всех коллекций
        product = self.get_object()   #Берём объект
        return self.get_queryset().filter(collection=product.collection.id)   #можно писать collection или collection_id

    def nav(self):
        clothing = ClothingCategories.objects.all()
        return clothing


# class CategoryProductListView(ListView):
#     model = CategoryProduct
#     template_name = 'categories.html'
#     context_object_name = 'categories'
#     queryset = CategoryProduct.objects.all()


def category_product_list_view(request, category_clothing_id):
    category_clothing = ClothingCategories.objects.get(pk=category_clothing_id)
    category_products = CategoryProduct.objects.filter(client_category=category_clothing.id)
    clothing = ClothingCategories.objects.all()
    context = {'category_products': category_products,
               'clothing': clothing,
               }
    return render(request, 'categories.html', context)



class ClothingCategoriesView(ListView):
    model = ClothingCategories
    template_name = 'categories_global.html'
    context_object_name = 'categories_clothing'
    queryset = ClothingCategories.objects.all()


class FirstPage(TemplateView):
    template_name = 'first_page2.html'

    def get_context_data(self, **kwargs):
        set_categories_clothing = {client_category: client_category.categoryproduct_set.all() for client_category in ClothingCategories.objects.filter()}
        context = super().get_context_data(**kwargs)
        # context['all_categories'] = set_categories_clothing
        news = News.objects.all()
        last_news = list(news[:1])
        next_news = list(news[1:4])
        context = {
            'all_categories': set_categories_clothing,
            'news': news,
            'last_news': last_news,
            'next_news': next_news,
        }
        return context


def search(request):
    search_query = request.GET.get('search', '') # передаётся имя ввода (строка поиска)

   #TODO Переписать на теги
    all_categories = {client_category: client_category.categoryproduct_set.all() for client_category in ClothingCategories.objects.filter()}
    news = News.objects.all()
    last_news = list(news[:1])
    next_news = list(news[1:4])

# если значение search_query существует (в строку поиска введён текст) ищем в нужных полях введённый текст
    if search_query:
        # Q(позволяет илспользовать "И", "ИЛИ")
        products = Product.objects.filter(Q(name__icontains=search_query) | Q(name__icontains=search_query.capitalize())
                                   | Q(name__icontains=search_query.casefold()))
    else:
        products = Product.objects.all()
    context = {'products': products,
               'all_categories': all_categories,
               'last_news': last_news,
               'next_news': next_news,
               'news': news,
               }
    return render(request, 'search.html', context)


@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Favorites.objects.get_or_create(user=request.user, product=Product)
            else:
                Favorites.objects.filter(user=request.user, product=Product).delete()
            return JsonResponse({'status': 'ok'})
        except Product.DoesNotExist:
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'error'})


@login_required
def add_subscribe(request):
    user = request.user
    product = Product.objects.get(pk=request.POST['id_cat'])
    subscribe = Favorites(user=user, product=product)
    subscribe.save()
    return redirect(f'/shop/product/{product.id}/')