from crispy_forms.helper import FormHelper
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.shortcuts import reverse

from mainapp.models import *



# class ProductFormAdmin(ModelForm):
#
#     def clean_product(self):
#
#         product = Product.objects.filter(category=self.instance)
#
#         if len(product) > 0 and self.cleaned_data['category'] != product[0]:
#             raise ValidationError(
#                 'Не является продуктом данной категории',
#                 code='invalid'
#             )
#
#         return self.cleaned_data['category']

# class ProductForm(ModelForm):
#
#     class Meta:
#         model = Product
#
#     def __int__(self, *args, **kwargs):
#         super(ProductForm, self).__int__(*args, **kwargs)
#
#         self.helper = FormHelper(self)
#         self.helper.form_method = 'POST'
#         self.helper.form_method = "form-forizontal"
#
#         add_form = True if not kwargs['instance'] else False
#
#         if add_form:
#             self.helper.form_action = reverse('product_add')
#         else:
#             self.helper.form_action = reverse(
#                 'product_edit',
#                 kwargs={'pk': kwargs['instance'].id}
#             )
#
#
class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].empty_label = 'Компания не выбрана'
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description',
            'category',
            'company',
            'image',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
