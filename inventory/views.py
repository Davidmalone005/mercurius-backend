import random

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import (
    Category,
    FlashsaleCtrl,
    LowerSubcategory,
    Product,
    ProductType,
    Subcategory,
)
from .serializers import (
    CategorySerializer,
    FlashsaleCtrlSerializer,
    LowerSubcategorySerializer,
    ProductSerializer,
    ProductTypeSerializer,
    SubcategorySerializer,
)

# Create your views here.


class AllCategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        seriData = serializer.data

        response = reversed(seriData)
        return Response(data=response, status=status.HTTP_200_OK)


class SingleCategoryView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class AllLowerSubcategoryView(ListCreateAPIView):
    queryset = LowerSubcategory.objects.all()
    serializer_class = LowerSubcategorySerializer

    def get(self, request, *args, **kwargs):
        queryset = LowerSubcategory.objects.all()
        serializer = LowerSubcategorySerializer(queryset, many=True)
        seriData = serializer.data

        response = reversed(seriData)
        return Response(data=response, status=status.HTTP_200_OK)


class SingleLowerSubcategoryView(RetrieveAPIView):
    queryset = LowerSubcategory.objects.all()
    serializer_class = LowerSubcategorySerializer
    lookup_field = 'slug'


class AllSubcategoryView(ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

    def get(self, request, *args, **kwargs):
        queryset = Subcategory.objects.all()
        serializer = SubcategorySerializer(queryset, many=True)
        seriData = serializer.data

        response = reversed(seriData)
        return Response(data=response, status=status.HTTP_200_OK)


class SingleSubcategoryView(RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    lookup_field = 'slug'

class AllProductsView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        response = random.sample(serializer.data, len(serializer.data))
        return Response(data=response, status=status.HTTP_200_OK)

        # return super().get(request, *args, **kwargs)


class SingleProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class AllFlashsaleView(ListCreateAPIView):
    queryset = FlashsaleCtrl.objects.all().filter(is_active=True)
    serializer_class = FlashsaleCtrlSerializer


class DisableFlashsalesView(ListCreateAPIView):
    queryset = Product.objects.all().filter(is_onFlashsale=True)
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        Product.objects.all().filter(is_onFlashsale=True).update(is_onFlashsale=False)

        # serializer = ProductSerializer(queryset, many=True)

        response = {"Is flashsale disabled?": "Yes"}

        return Response(data=response, status=status.HTTP_200_OK)


class AllFlashsaleProductsView(ListCreateAPIView):
    queryset = Product.objects.all().filter(is_onFlashsale=True)
    serializer_class = ProductSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all().filter(is_onFlashsale=True)
        serializer = ProductSerializer(queryset, many=True)
        response = random.sample(serializer.data, len(serializer.data))
        return Response(data=response, status=status.HTTP_200_OK)

class AllProductTypes(ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = queryset = ProductType.objects.all()
        serializer = ProductTypeSerializer(queryset, many=True)
        # response = random.sample(serializer.data, len(serializer.data))
        # response = random.sample(serializer.data, len(serializer.data))
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        # return Response(data=response, status=status.HTTP_200_OK)


