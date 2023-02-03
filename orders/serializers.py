from rest_framework import serializers
from rest_framework.validators import ValidationError

from users.models import User

from .models import Coupon, Order, OrderedItem, ShippingRate, Storehouse


class OrderedItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    qty = serializers.IntegerField()
    defaultImage = serializers.CharField()

    class Meta:
        model = OrderedItem
        fields = [
            "id",
            "user",
            "order",
            "name",
            "description",
            "price",
            "qty",
            "size",
            "defaultImage",
        ]


class StorehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storehouse
        fields = "__all__"

    # user = serializers.StringRelatedField()
    # storehouse_order = OrderSerializer()


class UpdateStorehouseSerializer(serializers.ModelSerializer):
    transaction_id = serializers.CharField()
    reference = serializers.CharField()
    shipping_fee = serializers.IntegerField()
    sales_tax = serializers.IntegerField()
    storehouse_billings = serializers.IntegerField()
    total_amount = serializers.IntegerField()
    has_been_paid = serializers.BooleanField()
    paid_at = serializers.DateTimeField()
    

    class Meta:
        model = Storehouse
        fields = ["transaction_id", "reference", "shipping_fee", "sales_tax", "storehouse_billings", "total_amount", "has_been_paid", "paid_at"]

    def update(self, instance, validated_data):
        instance.transaction_id = validated_data.get("transaction_id", instance.transaction_id)
        instance.reference = validated_data.get("reference", instance.reference)
        instance.shipping_fee = validated_data.get("shipping_fee", instance.shipping_fee)
        instance.sales_tax = validated_data.get("sales_tax", instance.sales_tax)
        instance.storehouse_billings = validated_data.get("storehouse_billings", instance.storehouse_billings)
        instance.total_amount = validated_data.get("total_amount", instance.total_amount)
        instance.has_been_paid = validated_data.get("has_been_paid", instance.has_been_paid)
        instance.paid_at = validated_data.get("paid_at", instance.paid_at)

        instance.save()

        return instance




class OrderSerializer(serializers.ModelSerializer):
    paystack_customer_code = serializers.CharField(max_length=40)
    transaction_id = serializers.CharField(max_length=20)
    reference = serializers.CharField(max_length=27)
    amount = serializers.IntegerField()
    shipping_fee = serializers.IntegerField()
    sales_tax = serializers.IntegerField()
    payment_method = serializers.CharField(max_length=27)
    payment_type = serializers.CharField(max_length=30)
    currency = serializers.CharField(max_length=27)
    paid_at = serializers.DateTimeField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Order
        fields = "__all__"


class OrderViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    user = serializers.StringRelatedField()
    ordered_items = OrderedItemSerializer(many=True)
    storehouse_order = StorehouseSerializer(many=True)


class ShippingRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingRate
        fields = "__all__"


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"
