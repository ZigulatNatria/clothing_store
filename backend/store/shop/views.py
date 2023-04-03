from django.shortcuts import render
from .models import Product, CategoryProduct, ClothingCategories, Collection, News
from django.views.generic import ListView, DetailView, TemplateView

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
    template_name = 'product_detail.html'
    context_object_name = 'product'
    queryset = Product.objects.all()

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
    template_name = 'first_page.html'

    def get_context_data(self, **kwargs):
        set_categories_clothing = {client_category: client_category.categoryproduct_set.all() for client_category in ClothingCategories.objects.filter()}
        context = super().get_context_data(**kwargs)
        # context['all_categories'] = set_categories_clothing
        news = News.objects.all()
        context = {
            'all_categories': set_categories_clothing,
            'news': news,
        }
        return context
