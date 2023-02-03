from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import APIView, api_view
from rest_framework.request import Request
from rest_framework.response import Response

from users.models import User

from .models import Coupon, Order, ShippingRate, Storehouse
from .serializers import (
    CouponSerializer,
    OrderSerializer,
    OrderViewSerializer,
    ShippingRateSerializer,
    StorehouseSerializer,
    UpdateStorehouseSerializer,
)


@api_view(http_method_names=["GET"])
def OrdersListAPIView(request: Request, pk):
    # def get(self, request, pk):
    user = User.objects.get(pk=pk)
    queryset = Order.objects.all().filter(user=user)
    serializer = OrderViewSerializer(instance=queryset, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def StorehouseListAPIView(request: Request, pk):
    user = User.objects.get(pk=pk)
    queryset = Storehouse.objects.all().filter(user=user)
    serializer = StorehouseSerializer(instance=queryset, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


# @api_view(http_method_names=["GET"])
# def UpdateStorehouseOrderAPIView(request: Request, pk, pk2):
#     user = User.objects.get(pk=pk)
#     queryset = Storehouse.objects.all().filter(user=user)
#     serializer = StorehouseSerializer(instance=queryset, many=True)

#     return Response(data=serializer.data, status=status.HTTP_200_OK)


class UpdateStorehouseOrderAPIViewAPIView(APIView):
    def post(self, request, pk, pk2, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        storeorder = get_object_or_404(Storehouse, pk=pk2)
        data = request.data


        orderDetail = {
            "id": 9,
            "transaction_id": data["transaction_id"],
            "reference": data["reference"],
            "shipping_fee": data["shipping_fee"],
            "sales_tax": data["sales_tax"],
            "billing_starts": "2023-02-09T07:06:21.807853+01:00",
            "storehouse_billings": data["storehouse_billings"],
            "total_amount": data["total_amount"],
            "created_at": "2023-01-26T07:06:24.905047+01:00",
            "has_been_paid": True,
            "paid_at": data["paid_at"],
            "user": 2,
            "order": 30,
        }

        serializer = UpdateStorehouseSerializer(instance=storeorder, data=orderDetail)

        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()

            response = {
                "success": "Updated Successfully",
                "data": serializer.validated_data,
            }

            return Response(data=response, status=status.HTTP_200_OK)

        return Response(
            data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class AllShippingRatesAPIView(generics.ListAPIView):
    queryset = ShippingRate.objects.all()
    serializer_class = ShippingRateSerializer


class SingleShippingRateAPIView(generics.RetrieveAPIView):
    queryset = ShippingRate.objects.all()
    serializer_class = ShippingRateSerializer
    lookup_field = "state"


class AllCouponCodesAPIView(generics.ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class SingleCouponCodeAPIView(generics.RetrieveAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    lookup_field = "coupon_code"


class DisableCouponCode(generics.GenericAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    def get(self, request, coupon_code, *args, **kwargs):
        Coupon.objects.all().filter(coupon_code=coupon_code).update(
            is_used=True
        )

        response = {"status": "Disabled"}

        return Response(data=response, status=status.HTTP_200_OK)
