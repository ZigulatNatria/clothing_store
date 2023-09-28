from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class ClientCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='название категории (М/Ж)')

    class Meta:
        verbose_name = 'Категория клиентов (М Ж)'
        verbose_name_plural = 'категории клиентов (М Ж)'

    def __str__(self):
        return self.name


class ClothingCategories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='название раздела категории одежды')
    client_category = models.ForeignKey('ClientCategory', on_delete=models.CASCADE, verbose_name='мужская или женская')
    photo = models.ImageField(verbose_name='фото категрии', null=True, blank=True)

    class Meta:
        verbose_name = 'раздел категории одежды'
        verbose_name_plural = 'разделы категорий одежды'

    def __str__(self):
        return self.name


class CategoryProduct(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='категория одежды')
    photo = models.ImageField(verbose_name='фото категрии', null=True, blank=True)
    client_category = models.ForeignKey('ClothingCategories', on_delete=models.CASCADE, verbose_name='раздел категории одежды')
    popular = models.BooleanField(default=False, verbose_name='популярное')

    class Meta:
        verbose_name = 'категория одежды'
        verbose_name_plural = 'категории одежды'

    def __str__(self):
        return self.name


class Stock(models.Model):
    quantity = models.CharField(max_length=50, unique=True, verbose_name='количество на складе')

    class Meta:
        verbose_name = 'наличие на складе'
        verbose_name_plural = 'наличие на складах'

    def __str__(self):
        return self.quantity


class Collection(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='название коллекции')

    class Meta:
        verbose_name = 'коллекция'
        verbose_name_plural = 'коллекции'

    def __str__(self):
        return self.name


# class Product(models.Model):
#     photo_1 = models.ImageField(verbose_name='Фото 1', blank=True, null=True)
#     photo_2 = models.ImageField(verbose_name='Фото 2', blank=True, null=True)
#     photo_3 = models.ImageField(verbose_name='Фото 3', blank=True, null=True)
#     photo_4 = models.ImageField(verbose_name='Фото 4', blank=True, null=True)
#     photo_5 = models.ImageField(verbose_name='Фото 5', blank=True, null=True)
#     name = models.CharField(max_length=100, verbose_name='Наименование товара')
#     vendor_code = models.CharField(max_length=100, unique=True, verbose_name='Артикул')
#     price = models.FloatField(verbose_name='цена')
#     colors = models.TextField(verbose_name='цвет')
#     size = models.TextField(verbose_name='размер')
#     stock_availability = models.ForeignKey('Stock', on_delete=models.CASCADE, verbose_name='Наличие на складе', null=True, blank=True)
#     description = models.TextField(verbose_name='Описание товара')
#     compound = models.TextField(verbose_name='Состав и уход')
#     size_on_model = models.TextField(verbose_name='Размер модели\размер на модели')
#     collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name='Коллекция', null=True, blank=True)
#     category_product = models.ForeignKey('CategoryProduct', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория одежды')
#     #TODO возможно докинуть поля связанные с категриями ClothingCategories, ClientCategory
#
#     class Meta:
#         verbose_name = 'Товар'
#
#     def __str__(self):
#         return self.name


class Color(models.Model):
    vendor_code = models.CharField(max_length=100, verbose_name='артикул товара')
    name_color = models.CharField(max_length=100, verbose_name='название цвета')
    photo_1 = models.ImageField(verbose_name='фото 1')
    photo_2 = models.ImageField(verbose_name='фото 2')
    photo_3 = models.ImageField(verbose_name='фото 3')
    photo_4 = models.ImageField(verbose_name='фото 4')
    photo_5 = models.ImageField(verbose_name='фото 5')

    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'

    def __str__(self):
        return '{}'.format(self.name_color) + 'цвет товара с артикулом' + ' ' + '{}'.format(self.vendor_code)


class Size(models.Model):
    vendor_code = models.CharField(max_length=100, verbose_name='артикул товара')
    size = models.CharField(max_length=100, unique=True, verbose_name='размер')

    class Meta:
        verbose_name = 'размер'
        verbose_name_plural = 'размеры'

    def __str__(self):
        return 'Размер товара с артикулом' + ' ' + '{}'.format(self.vendor_code)


class Product(models.Model):
    photo_1 = models.ImageField(verbose_name='фото 1')
    photo_2 = models.ImageField(verbose_name='фото 2')
    photo_3 = models.ImageField(verbose_name='фото 3')
    photo_4 = models.ImageField(verbose_name='фото 4')
    photo_5 = models.ImageField(verbose_name='фото 5')
    name = models.CharField(max_length=100, verbose_name='наименование товара')
    vendor_code = models.CharField(max_length=100, unique=True, verbose_name='артикул')
    price = models.FloatField(verbose_name='цена')
    colors = models.ManyToManyField(Color, verbose_name='цвета', blank=True)
    size = models.ManyToManyField(Size, verbose_name='размеры', blank=True)
    stock_availability = models.ForeignKey(
        'Stock',
        on_delete=models.CASCADE,
        verbose_name='наличие на складе',
        null=True,
        blank=True
    )
    description = models.TextField(verbose_name='описание товара')
    compound = models.TextField(verbose_name='состав и уход')
    size_on_model = models.TextField(verbose_name='размер модели\размер на модели')
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        verbose_name='коллекция',
        null=True,
        blank=True
    )
    category_product = models.ForeignKey(
        'CategoryProduct',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='категория одежды'
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[AbstractUser.username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        null=True,
        blank=True,
    )

    email = models.EmailField(_("email address"), unique=True, )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        # 'username'   #раскомментить при создании суперюзера!!!!
    ]

    favorite_products = models.ManyToManyField(Product, verbose_name='избранное')


class News(models.Model):
    header = models.CharField(max_length=100, verbose_name='заголовок новости')
    text = models.TextField(verbose_name='текст новости')
    author = models.CharField(max_length=50, verbose_name='автор новости')
    date_add = models.DateField(auto_now=True)
    image = models.ImageField(verbose_name='фото новости')

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['-id']

    def __str__(self):
        return self.header


class Favorites(models.Model):
    # user = models.ForeignKey('auth.User', related_name='пользователь', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='пользователь', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', related_name='товар', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'избранное'
        verbose_name_plural = 'избранные'
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return f'{self.user} follows {self.product}'


# user_model = get_user_model()
# user_model.add_to_class(
#     'following',
#     models.ManyToManyField('self',
#                            through=Favorites,
#                            related_name='Избранное',
#                            symmetrical=False)
# )