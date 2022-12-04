from django.shortcuts import render
from .models import Category
from .models import Product

def main(request):
    return render(request, 'index.html')

def Category_list(request):

    category = Category.objects.filter(id=1)

    context = {'category': category}

    return render(request, 'category_list.html', context)

# def Product_list(request):
#
#     product = Product.objects.filter()
#
#     context = {'product': product}
#
#     return render(request, 'Mobile.html', context)



