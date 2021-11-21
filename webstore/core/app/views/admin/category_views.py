from django.shortcuts import render
from django.views import View
import requests
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from var_dump import var_dump


class CategoryListView(View):
    @staticmethod
    def get(request):
        get_request = requests.get('http://127.0.0.1:8080/api/categories/')
        categories = []
        if get_request.status_code == 200:
            categories = get_request.json()
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
            'sidebar_active': 'sidebar_categories',
        }
        return render(request, 'admin/add_category.html', data)

    @staticmethod
    def post(request):
        data = {
            'page_title': 'Add category',
            'sidebar_active': 'sidebar_categories',
        }

        res = requests.post('http://127.0.0.1:8080/api/categories/', request.POST)
        print(res.json())
        return render(request, 'admin/add_category.html', data)
