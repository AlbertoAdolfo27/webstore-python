from django.shortcuts import render
from django.views import View
import requests
from rest_framework import status

from core.app.utils.Server import Server


class ProductListView(View):
    @staticmethod
    def get(request):
        response = requests.get(Server.get_url('api:product-list'))
        products = []
        if response.status_code == 200:
            products = response.json()
        data = {
            'page_title': 'products',
            'sidebar_active': 'sidebar_products',
            'products': products,
        }
        return render(request, 'admin/products.html', data)
