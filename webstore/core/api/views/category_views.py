from django.http import Http404
from rest_framework.response import Response

from core.api.models import Category, Product
from core.api.serializers import CategorySerializer, ProductSerializer
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


# Category Detail
class CategoryDetailView(APIView):
    # Query Category
    @staticmethod
    def get_object(pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    # Detail category by GET method
    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryProductsViews(APIView):
    @staticmethod
    def get(request, pk):
        products = CategoryDetailView.get_object(pk).products.all()
        serializer = ProductSerializer(products,  many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryProductsNotInViews(APIView):
    @staticmethod
    def get(request, pk):
        products = Product.objects.exclude(
            pk__in=CategoryDetailView.get_object(pk).products.all()
        )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
