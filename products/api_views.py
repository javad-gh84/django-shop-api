from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Products
from .serializers import ProductSerializer


class ProductListAPIView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
