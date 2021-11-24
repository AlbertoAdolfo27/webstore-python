from django.http import Http404
from rest_framework.views import APIView
from core.api.serializers import ProductSerializer
from core.api.models import Product
from rest_framework.response import Response
from rest_framework import status


class ProductView(APIView):
    @staticmethod
    def get(request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create product by post method
    @staticmethod
    def post(request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Product Detail
class ProductDetailView(APIView):

    # Query product
    @staticmethod
    def get_object(pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    # Detail Product by GET method
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)