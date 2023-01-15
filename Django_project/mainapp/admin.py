from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.shortcuts import render, get_object_or_404
from django.utils.html import format_html
# from .forms import ProductFormAdmin
from .models import Category, Product, Company

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    ordering = ['name']
    list_per_page = 5
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'available',
        'category',
        # 'view_product_link',
        'ava',
    ]
    list_display_links = ['name', 'price']
    list_editable = ['category', 'available']
    list_filter = ['category', 'available']
    prepopulated_fields = {'slug': ('name',) }
    list_per_page = 5
    search_fields = ['name', 'price']
    ordering = ['price']
    # form = ProductFormAdmin

    @staticmethod
    def ava(obj):
        return mark_safe(f"<img class='img-circle' src='{obj.image.url}'"
                         f"height='30' widht='30'>"
        )

    # @staticmethod
    # def view_product_link(request, obj):
    #     product = get_object_or_404(obj, slug=obj.slug)
    #     context = {
    #         'product': product,
    #     }
    #     return render(request, 'Product.html', context)


    # @staticmethod
    # def custom_field(obj):
    #     return mark_safe(f'<a href="{obj.get_absolute_url}/{obj.slug}">кнопка</a>')

    # @staticmethod
    # def view_on_site(self, obj):
    #     return reverse('product_edit', kwargs={'pk': obj.pk})

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    ordering = ['name']
    list_per_page = 5
    list_filter = ['name']