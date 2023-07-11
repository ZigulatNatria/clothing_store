from django.contrib import admin
from .models import ClientCategory, ClothingCategories, CategoryProduct, Stock, \
    Collection, Product, News, Color, Size, Favorites

# Register your models here.
admin.site.register(ClientCategory)
admin.site.register(ClothingCategories)
admin.site.register(CategoryProduct)
admin.site.register(Stock)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(News)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Favorites)