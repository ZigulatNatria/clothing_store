from django.db import models

# Create your models here.
class ClientCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория клиентов (М Ж)'

    def __str__(self):
        return self.name


class ClothingCategories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название раздела категории одежды')
    client_category = models.ForeignKey('ClientCategory', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Раздел категории одежды'

    def __str__(self):
        return self.name


class CategoryProduct(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория одежды')
    photo = models.ImageField(verbose_name='Фото категрии', null=True, blank=True)
    client_category = models.ForeignKey('ClothingCategories', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Категория одежды'

    def __str__(self):
        return self.name


class Stock(models.Model):
    quantity = models.CharField(max_length=50, verbose_name='количество на складе')

    class Meta:
        verbose_name = 'Наличие на складе'

    def __str__(self):
        return self.quantity


class Collection(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название коллекции')

    class Meta:
        verbose_name = 'Коллекция'

    def __str__(self):
        return self.name


class Product(models.Model):
    photo_1 = models.ImageField(verbose_name='Фото 1', blank=True, null=True)
    photo_2 = models.ImageField(verbose_name='Фото 2', blank=True, null=True)
    photo_3 = models.ImageField(verbose_name='Фото 3', blank=True, null=True)
    photo_4 = models.ImageField(verbose_name='Фото 4', blank=True, null=True)
    photo_5 = models.ImageField(verbose_name='Фото 5', blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Наименование товара')
    vendor_code = models.CharField(max_length=100, unique=True, verbose_name='Артикул')
    price = models.FloatField(verbose_name='цена')
    colors = models.TextField(verbose_name='цвет') #TODO ссылки/картинки на другой аналогичный товар
    size = models.TextField(verbose_name='размер') #TODO выпадающий список
    stock_availability = models.ForeignKey('Stock', on_delete=models.CASCADE, verbose_name='Наличие на складе')
    description = models.TextField(verbose_name='Описание товара')
    compound = models.TextField(verbose_name='Состав и уход')
    size_on_model = models.TextField(verbose_name='Размер модели\размер на модели')
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE, verbose_name='Коллекция')
    category_product = models.ForeignKey('CategoryProduct', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория одежды')
    #TODO возможно докинуть поля связанные с категриями ClothingCategories, ClientCategory

    class Meta:
        verbose_name = 'Товар'

    def __str__(self):
        return self.name

