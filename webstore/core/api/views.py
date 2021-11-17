from django.http import JsonResponse
from core.api.models import Category
from core.api.serializers import CategorySerializer
from rest_framework import status
from rest_framework.views import APIView


class CategoryView(APIView):

    @staticmethod
    def get(request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        data = serializer.data

        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
