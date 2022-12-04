from django.urls import path
from . import views


urlpatterns = [
    path('', views.main),
    path('Catalog/', views.Category_list),
    #path('Catalog/Mobil/', views.Product_list)
]
