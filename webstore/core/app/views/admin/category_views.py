from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
import requests
from rest_framework import status
from core.app.utils.Server import Server


# List all Categories
class CategoryListView(View):
    @staticmethod
    def get(request):
        categories = []
        response = requests.get(Server.get_url('api:category'))
        if response.status_code == 200:
            categories = response.json()
        data = {
            'page_title': 'Categories',
            'sidebar_active': 'sidebar_categories',
            'categories': categories,
        }
        return render(request, 'admin/categories.html', data)


# Add new Category
class CategoryAddView(View):
    # Render HTML page
    @staticmethod
    def get(request):
        data = {
            'page_title': 'Add category',
            'sidebar_active': 'sidebar_categories'
        }
        return render(request, 'admin/add_category.html', data)

    # Add new category by POST method
    @staticmethod
    def post(request):
        category = []
        errors = []
        response = requests.post(Server.get_url('api:category'), request.POST)
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


# Detail a category
class CategoryDetailView(View):
    @staticmethod
    def get(request, pk):
        products_not_in = []
        products = []
        category = []
        errors = []
        response = requests.get(Server.get_url('api:category-detail', [pk]))
        if response.status_code == status.HTTP_200_OK:
            category = response.json()
            products = requests.get(Server.get_url('api:category-products', [pk])).json()
            products_not_in = requests.get(Server.get_url('api:category-products-not-in', [pk])).json()
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
        return render(request, 'admin/category_detail.html', data)


# Relate product to category
class CategoryProductsRelateView(View):
    @staticmethod
    def get(request, pk_category, pk_product):
        response = requests.get(Server.get_url('api:category-product-relate', [pk_category, pk_product]))
        if response.status_code == status.HTTP_200_OK:
            return HttpResponseRedirect(reverse('app:admin-category-detail', args=[pk_category]))


# Remove product from category
class CategoryProductsRemoveRelationView(View):
    @staticmethod
    def get(request, pk_category, pk_product):
        response = requests.get(Server.get_url('api:category-product-remove-relation', [pk_category, pk_product]))
        if response.status_code == status.HTTP_200_OK:
            return HttpResponseRedirect(reverse('app:admin-category-detail', args=[pk_category]))
