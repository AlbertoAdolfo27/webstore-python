from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from core.api.models import Category


class CategoryView(View):

    @staticmethod
    def get(request):
        categories = Category.objects.all()
        data = {
            'page_name': 'Categories',
            'categories': categories
        }

        return render(request, 'admin/categories.html', data)
