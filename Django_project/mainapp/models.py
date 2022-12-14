from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,
                            db_index=True,
                            verbose_name='Название категории',
                            )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.PROTECT)

    name = models.CharField(max_length=150,
                            db_index=True,
                            verbose_name=u'Название',
                            )

    image = models.ImageField(upload_to='product/%Y/%m/%d',
                              blank=True,
                              verbose_name=u'Фото'
                              )

    description = models.TextField(max_length=1000,
                                   blank=True,
                                   verbose_name=u'Описание')

    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name=u'Цена',
                                )

    available = models.BooleanField(default=True,
                                    verbose_name=u'Наличие',
                                    )

    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name=u'Дата создания',
                                   )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
