from django.contrib import admin
from .models import ClientCategory, ClothingCategories, CategoryProduct, Stock, \
    Collection, Product, News, Color, Size, Favorites
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(ClientCategory)
admin.site.register(ClothingCategories)
admin.site.register(CategoryProduct)
admin.site.register(Stock)
admin.site.register(Collection)
# admin.site.register(Product)
admin.site.register(News)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Favorites)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'get_image',
        'vendor_code',
        'price',
        # 'stock_availability',
        # 'description',
        # 'compound',
        # 'size_on_model',
        # 'collection',
        'category_product',
    ]
    list_filter = [
        'name',
        'vendor_code',
    ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo_1.url} width="50" height="60"')

    get_image.short_description = 'Изображение'
    # list_editable = ['price', 'name']
    # prepopulated_fields = {'slug': ('name',)}