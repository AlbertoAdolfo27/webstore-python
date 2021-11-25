from django.shortcuts import render
from django.views import View
import requests
from rest_framework import status

from core.app.utils.Server import Server


class ProductListView(View):
    @staticmethod
    def get(request):
        response = requests.get(Server.get_url('api:product'))
        products = []
        if response.status_code == 200:
            products = response.json()
        data = {
            'page_title': 'Products',
            'sidebar_active': {
                'link_1': 'sb_link_products',
                'link_2': 'sb_link_products_list',
            },
            'products': products,
        }
        return render(request, 'admin/products.html', data)


class ProductAddView(View):
    @staticmethod
    def get(request):
        data = {
            'page_title': 'Add product',
            'sidebar_active': {
                'link_1': 'sb_link_products',
                'link_2': 'sb_link_products_add',
            },
        }
        return render(request, 'admin/add_product.html', data)

    @staticmethod
    def post(request):
        response = requests.post(Server.get_url('api:product'), request.POST)
        product = []
        errors = []
        if response.status_code == status.HTTP_201_CREATED:
            product = response.json()
        else:
            errors = response.json()
        data = {
            'page_title': 'Add product',
            'sidebar_active': {
                'link_1': 'sb_link_products',
                'link_2': 'sb_link_products_add',
            },
            'product': product,
            'status_code': response.status_code,
            'errors': errors,
        }
        return render(request, 'admin/add_product.html', data)


class ProductDetailView(View):
    @staticmethod
    def get(request, pk):

        response = requests.get(Server.get_url('api:product-detail', pk))
        product = []
        errors = []
        if response.status_code == status.HTTP_200_OK:
            product = response.json()
        else:
            errors = response.json()
        data = {
            'page_title': 'Product detail',
            'sidebar_active': {
                'link_1': 'sb_link_products',
                'link_2': 'sb_link_products_list',
            },
            'product': product,
            'status_code': response.status_code,
            'errors': errors,
        }
        return render(request, 'admin/product_detail.html', data)

