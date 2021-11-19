from django.shortcuts import render
from django.views import View
import requests


class IndexView(View):

    @staticmethod
    def get(request):
        get_request = requests.get('http://127.0.0.1:8080/api/categories')
        categories = []
        if get_request.status_code == 200:
            categories = get_request.json()

        data = {
            'page_title': 'Web store - Home page',
            'categories': categories
        }
        return render(request, 'index.html', data)


