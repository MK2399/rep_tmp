from django.urls import path
from mainapp.views import *


urlpatterns = [
    path('', ProductHome.as_view(), name='Home'),
    path('about/', about, name='About'),
    path('catalog/<slug:category_slug>/', ShopCategory.as_view(), name='Catalog'),
    path('product/<slug:product_slug>/', ShowDetail.as_view(), name='product'),
    path('add_product/', AddPage.as_view(), name='add_product'),
]
