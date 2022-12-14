# from django.core.paginator import Paginator
# from django.core.paginator import PageNotAnInteger
# from django.core.paginator import EmptyPage
#
# def get_current_category(request):
#
#     from .models import Category
#
#     pk = request.COOKIES.get('current_category')
#
#     if pk:
#         try:
#             category = Category.objects.get(pk=int(pk))
#         except Category.DoesNotExist:
#             return None
#         return category
#
# def paginate(obj: object,
#              size: int,
#              request: object,
#              context: dict,
#              var_name: str = 'object_list',
# ):
#
#     paginator = Paginator(obj, size)
#     page = request.GET.get('page', 1)
#
#     try:
#         object_list = paginator.page(page)
#     except PageNotAnInteger:
#         object_list = paginator.page(1)
#
#     except EmptyPage:
#         object_list = paginator.page(paginator.num_pages)
#
#     context[var_name] = object_list
#     context['is_paginated'] = object_list.has_other_pages()
#     context['page_obj'] = object_list
#     context['paginator'] = paginator
