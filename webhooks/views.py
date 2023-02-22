import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from orders.models import Order, OrderedItem, Storehouse
from orders.serializers import (
    OrderedItemSerializer,
    OrderSerializer,
    StorehouseSerializer,
    UpdateStorehouseSerializer,
)
from users.models import User

from .models import Webhook
from .serializers import WebhookSerializer


@csrf_exempt
def PaystackWebhookAPIView(request):
    if request.method == "POST":
        body = request.body
        data = {}

        try:
            data = json.loads(body)
        except:
            pass

        if (
            data["event"] == "charge.success"
            or data["event"] == "transfer.success"
        ):

            paymentTypeStatus = data["data"]["metadata"]["paymentType"]

            print(paymentTypeStatus)

            user_id = data["data"]["metadata"]["user_id"]
            user = User.objects.get(pk=user_id)

            if (
                paymentTypeStatus == "Ship All Orders"
                or paymentTypeStatus == "Ship Order"
            ):
                print("---------From Storehouse...")

                storehouse_item_ids = data["data"]["metadata"][
                    "storehouse_items"
                ]

                if len(storehouse_item_ids) > 0:
                    user_id = data["data"]["metadata"]["user_id"]

                    for si in storehouse_item_ids:
                        so = get_object_or_404(Storehouse, pk=si)

                        orderDetail = {
                            "id": si,
                            "transaction_id": data["data"]["id"],
                            "reference": data["data"]["reference"],
                            "shipping_fee": 0,
                            "sales_tax": 0,
                            "billing_starts": so.billing_starts,
                            "storehouse_billings": 0,
                            "total_amount": data["data"]["metadata"][
                                "totalAmount"
                            ],
                            "created_at": data["data"]["created_at"],
                            "has_been_paid": True,
                            "paid_at": data["data"]["paid_at"],
                            "user": user_id,
                            "order": so.order.pk,
                            
                        }

                        serializer = UpdateStorehouseSerializer(
                            instance=so, data=orderDetail
                        )

                        if serializer.is_valid():
                            serializer.save()
                        else:
                            print(serializer.errors)

                else:
                    user_id = data["data"]["metadata"]["user_id"]
                    order_id = data["data"]["metadata"]["order_id"]
                    storehouse_order_id = data["data"]["metadata"][
                        "storehouse_order_id"
                    ]
                    user = get_object_or_404(User, pk=user_id)
                    storeorder = get_object_or_404(
                        Storehouse, pk=storehouse_order_id
                    )

                    orderDetail = {
                        "id": data["data"]["metadata"]["storehouse_order_id"],
                        "transaction_id": data["data"]["id"],
                        "reference": data["data"]["reference"],
                        "shipping_fee": data["data"]["metadata"]["shippingFee"],
                        "sales_tax": data["data"]["metadata"]["salesTax"],
                        "billing_starts": data["data"]["metadata"][
                            "billing_starts"
                        ],
                        "storehouse_billings": data["data"]["metadata"][
                            "storehouse_billings"
                        ],
                        "total_amount": data["data"]["metadata"]["totalAmount"],
                        "created_at": data["data"]["created_at"],
                        "has_been_paid": True,
                        "paid_at": data["data"]["paid_at"],
                        "user": user_id,
                        "order": order_id,
                        "used_coupon": "No"
                    }

                    serializer = UpdateStorehouseSerializer(
                        instance=storeorder, data=orderDetail
                    )

                    if serializer.is_valid():
                        serializer.save()

            else:
                amountTotal = data["data"]["amount"] / 100

                orderedItems = data["data"]["metadata"]["cart"]
                
                used_coupon = data["data"]["metadata"]["used_coupon"]

                if orderedItems:
                    orderDetails = {
                        "user": data["data"]["metadata"]["user_id"],
                        "paystack_customer_code": data["data"]["customer"][
                            "customer_code"
                        ],
                        "transaction_id": data["data"]["id"],
                        "reference": data["data"]["reference"],
                        "amount": amountTotal,
                        "shipping_fee": data["data"]["metadata"]["shippingFee"],
                        "sales_tax": data["data"]["metadata"]["salesTax"],
                        "coupon": data["data"]["metadata"]["discount"],
                        "payment_method": data["data"]["channel"],
                        "payment_type": data["data"]["metadata"]["paymentType"],
                        "currency": data["data"]["currency"],
                        "paid_at": data["data"]["paid_at"],
                        "created_at": data["data"]["created_at"],
                        "used_coupon": used_coupon,
                    }

                    serializer = OrderSerializer(data=orderDetails)

                    if serializer.is_valid():
                        order = serializer.save(user=user)

                        for item in range(len(orderedItems)):
                            # print(orderedItems[item])
                            orderedItemDetail = {
                                "user": user_id,
                                "order": order.id,
                                "name": orderedItems[item]["name"],
                                "description": orderedItems[item][
                                    "description"
                                ],
                                "price": orderedItems[item]["price"],
                                "flashsale_price": orderedItems[item]["flashsale_price"],
                                "qty": orderedItems[item]["qty"],
                                "size": orderedItems[item]["size"],
                                "defaultImage": orderedItems[item][
                                    "defaultImage"
                                ],
                            }

                            serializer = OrderedItemSerializer(
                                data=orderedItemDetail
                            )

                            if serializer.is_valid():
                                savedItems = serializer.save(user=user)

                            else:
                                print(serializer.errors)

                        if data["data"]["metadata"]["paymentType"] == "Storage":
                            storehouseDetails = {
                                "user": data["data"]["metadata"]["user_id"],
                                "order": order.id,
                            }

                            serializer = StorehouseSerializer(
                                data=storehouseDetails
                            )

                            if serializer.is_valid():
                                saved2storehouse = serializer.save(user=user)
                            else:
                                print(serializer.errors)

                    else:
                        print(serializer.errors)
                else:
                    print("Paying for Storehouse Billings")

        return HttpResponse("Error loading...")
    return HttpResponse("Webhook waiting...")


@csrf_exempt
def PaystackCallbackUrlAPIView(request):
    if request.method == "POST":
        body = request.body
        data = {}

        try:
            data = json.loads(body)
        except:
            pass

        print(data)
