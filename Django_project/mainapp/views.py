from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddProductForm
from .models import Category
from .models import Product

class ProductHome(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My Shop'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Product.objects.filter(available=True)


# def index(request):
#
#     product = Product.objects.all()
#
#     context = {
#         'product': product,
#         'cat_selected': 0,
#     }
#     return render(request, 'index.html', context)

def about(request):

    return render(request, 'about.html')

class ShowDetail(DetailView):
    model = Product
    template_name = 'Product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = contex['product']
        return contex



# def show_detail(request, product_slug):
#
#     product = get_object_or_404(Product, slug=product_slug)
#
#     context = {
#         'product': product,
#         'cat_selected': product.category_id,
#         'title': 'Выбранный товар',
#     }
#
#     return render(request, 'Product.html', context)

class ShopCategory(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'product'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['product'][0].category)
        context['cat_selected'] = context['product'][0].category_id
        return context

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], available=True)




# def show_product(request, category_id):
#
#     product = Product.objects.filter(category_id=category_id)
#
#     context = {
#         'product': product,
#         'cat_selected': category_id,
#         'title': 'Категории товаров'
#     }
#
#     return render(request, 'index.html', context)

class AddPage(CreateView):
    form_class = AddProductForm
    template_name = 'add_product.html'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        success_url = reverse_lazy('home')
        context['title'] = 'Добавление товара'
        return context



# def add_product(request, LoginRequiredMixin):
#
#     if request.method == 'POST':
#         form = AddProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('Home')
#     else:
#         form = AddProductForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'add_product.html', context)
