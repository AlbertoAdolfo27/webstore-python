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
