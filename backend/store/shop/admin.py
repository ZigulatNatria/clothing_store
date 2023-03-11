from django.contrib import admin
from .models import ClientCategory, ClothingCategories, CategoryProduct, Stock, Collection, Product

# Register your models here.
admin.site.register(ClientCategory)
admin.site.register(ClothingCategories)
admin.site.register(CategoryProduct)
admin.site.register(Stock)
admin.site.register(Collection)
admin.site.register(Product)