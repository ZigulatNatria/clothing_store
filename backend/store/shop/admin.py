from django.contrib import admin
from .models import ClientCategory, ClothingCategories, CategoryProduct, Stock, \
    Collection, Product, News, Size, Favorites, CustomUser, Color
from django.utils.safestring import mark_safe


admin.site.register(ClientCategory)
admin.site.register(Stock)
admin.site.register(Favorites)
admin.site.register(CustomUser)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'get_image',
        'vendor_code',
        'price',
        'collection',
        'category_product',
    ]

    list_filter = [
        'name',
        'vendor_code',
        'category_product',
        'collection',
    ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo_1.url} width="50" height="70"')

    get_image.short_description = 'Изображение'
    # list_editable = ['price', 'name']
    # prepopulated_fields = {'slug': ('name',)}


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

    list_filter = [
        'name',
    ]


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = [
        'color',
    ]

    list_filter = [
        'color',
    ]


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = [
        'size',
    ]

    list_filter = [
        'size',
    ]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'header',
        'get_image',
        'author',
        'date_add',
    ]

    list_filter = [
        'header',
        'author',
        'date_add',
    ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="70" height="50"')

    get_image.short_description = 'Изображение'


@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'get_image',
        'client_category',
    ]

    list_filter = [
        'name',
        'client_category',
    ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="70"')

    get_image.short_description = 'Изображение'


@admin.register(ClothingCategories)
class ClothingCategoriesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'get_image',
        'client_category',
    ]

    list_filter = [
        'name',
        'client_category',
    ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="70"')

    get_image.short_description = 'Изображение'