from django.shortcuts import render
from django.views import View


class IndexView(View):

    @staticmethod
    def get(request):
        data = {
            'page_title': 'Home page'
        }
        return render(request, 'index.html', data)


