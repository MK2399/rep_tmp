from django.utils import timezone

from .models import *


class SoftDateTimeMixin:

    create_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=True,
    )

    update_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=True,
    )

    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

nav = [
    {'title': "О сайте", 'url_name': 'About'},
    {'title': "Добавление товара", 'url_name': 'add_product'},
    {'title': "О сайте", 'url_name': 'About'},
    ]

class ViewMixin:
    def get_context(self, **kwargs):
        context = kwargs
        category = Category.objects.all()
        product = Product.objects.all()
        context['nav'] = nav
        context['category'] = category
        context['product'] = product
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

