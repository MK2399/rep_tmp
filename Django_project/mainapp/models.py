from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from mainapp.mixins import SoftDateTimeMixin


class Category(SoftDateTimeMixin, models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='Название категории',
    )

    slug = models.SlugField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name=u'URL'
    )

    image = models.ImageField(
        blank=True,
        upload_to='img/'
    )

    def get_absolute_url(self):
        return reverse('Catalog', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Company(SoftDateTimeMixin, models.Model):

    class Meta:
        verbose_name = u'Компания'
        verbose_name_plural = u'Компании'

    name = models.CharField(
        max_length=30,
        verbose_name=u'Название компании'
    )

    def __str__(self):
        return self.name

class Product(SoftDateTimeMixin, models.Model):

    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.PROTECT,
        verbose_name=u'Категория'
    )

    name = models.CharField(
        max_length=150,
        db_index=True,
        verbose_name=u'Название',
    )

    image = models.ImageField(
        upload_to='product/%Y/%m/%d',
        blank=True,
        verbose_name=u'Фото'
    )

    description = models.TextField(
        max_length=1000,
        blank=True,
        verbose_name=u'Описание'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=u'Цена',
    )

    available = models.BooleanField(
        default=True,
        verbose_name=u'Наличие',
    )

    slug = models.SlugField(
        max_length=150,
        db_index=True,
        unique=True,
        verbose_name=u'URL'
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        null=True,
        verbose_name=u'Название компании'

    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Product, self).save(*args, **kwargs)

class User(SoftDateTimeMixin, models.Model):

    first_name = models.CharField(
        verbose_name=u'Имя',
        max_length=50,
        db_index=True,
    )

    last_name = models.CharField(
        verbose_name=u'Фамилия',
        max_length=50,
        db_index=True,
    )

    middle_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Отчество',
        default='',
    )

    birthday = models.DateTimeField(
        blank=False,
        null=True,
        verbose_name=u'Дата рождения'
    )

    photo = models.ImageField(
        blank=True,
        null=True,
        verbose_name=u'Фото',
        upload_to='users/'

    )