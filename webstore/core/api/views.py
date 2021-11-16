from django.http import JsonResponse
from django.views import View
from core.api.models import Category
from core.api.serializers import CategorySerializer


class CategoryView(View):

    @staticmethod
    def get(request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        data = serializer.data

        return JsonResponse(data, safe=False, status=200)
