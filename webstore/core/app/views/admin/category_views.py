from django.shortcuts import render
from django.views import View
import requests
from rest_framework import status

from core.app.utils.Server import Server


class CategoryListView(View):
    @staticmethod
    def get(request):
        response = requests.get(Server.get_url('api:category'))
        categories = []
        if response.status_code == 200:
            categories = response.json()
        data = {
            'page_title': 'Categories',
            'sidebar_active': 'sidebar_categories',
            'categories': categories,
        }
        return render(request, 'admin/categories.html', data)


class CategoryAddView(View):

    @staticmethod
    def get(request):
        data = {
            'page_title': 'Add category',
            'sidebar_active': 'sidebar_categories'
        }
        return render(request, 'admin/add_category.html', data)

    @staticmethod
    def post(request):
        response = requests.post(Server.get_url('api:category'), request.POST)
        category = []
        errors = []
        if response.status_code == status.HTTP_201_CREATED:
            category = response.json()
        else:
            errors = response.json()
        data = {
            'page_title': 'Add category',
            'sidebar_active': 'sidebar_categories',
            'category': category,
            'status_code': response.status_code,
            'errors': errors,
        }
        return render(request, 'admin/add_category.html', data)


class CategoryDetailView(View):
    @staticmethod
    def get(request, pk):

        response = requests.get(Server.get_url('api:category-detail', [pk]))
        products_not_in = []
        products = []
        category = []
        errors = []
        if response.status_code == status.HTTP_200_OK:
            category = response.json()
            products = requests.get(Server.get_url('api:category-products', [pk])).json()
            products_not_in = requests.get(Server.get_url('api:category-products-notin', [pk])).json()
        else:
            errors = response.json()
        print(products_not_in)
        data = {
            'page_title': 'Category detail',
            'sidebar_active': 'sidebar_categories',
            'category': category,
            'products': products,
            'products_not_in': products_not_in,
            'status_code': response.status_code,
            'errors': errors,
        }
        print(products)
        return render(request, 'admin/category_detail.html', data)
