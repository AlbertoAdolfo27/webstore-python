from rest_framework.response import Response

from core.api.models import Category
from core.api.serializers import CategorySerializer
from rest_framework import status
from rest_framework.views import APIView


class CategoryView(APIView):
    # List categories by get method
    @staticmethod
    def get(request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create category by post method
    @staticmethod
    def post(request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
