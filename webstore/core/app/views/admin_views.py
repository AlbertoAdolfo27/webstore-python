from django.shortcuts import render
from django.views import View
import requests


class IndexView(View):
    @staticmethod
    def get(request):
        get_request = requests.get('http://127.0.0.1:8080/api/categories/')
        categories = []
        if get_request.status_code == 200:
            categories = get_request.json()

        data = {
            'page_title': 'Admin - Dashboard',
            'categories': categories
        }
        return render(request, 'site/admin/index.html', data)


class CategoriesListView(View):
    @staticmethod
    def get(request):
        get_request = requests.get('http://127.0.0.1:8080/api/categories/')
        categories = []
        if get_request.status_code == 200:
            categories = get_request.json()

        data = {
            'request': request,
            'page_title': 'Categories',
            'categories': categories,
        }
        return render(request, 'site/admin/categories.html', data)
