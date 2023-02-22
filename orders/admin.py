from django.contrib import admin

from .models import Coupon, Order, OrderedItem, ShippingRate, Storehouse

# Register your models here.


class OrderItemInlineModel(admin.StackedInline):
    model = OrderedItem
    fields = [
        "name",
        "description",
        "price",
        "qty",
        "size",
        "defaultImage",
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "reference",
        "amount",
        "payment_type",
        "paid_at",
        "created_at",
    ]

    list_filter = ["payment_type", "payment_method", "paid_at"]

    inlines = [
        OrderItemInlineModel,
    ]

    search_fields = ["user", "reference", "amount", "payment_type"]


@admin.register(OrderedItem)
class OrderedItemAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "name",
        "description",
        "price",
        "qty",
        "size",
        "defaultImage",
        "ordered_at",
    ]

    list_filter = ["price", "qty", "size", "ordered_at"]

    search_fields = ["user", "name", "description", "price", "qty", "size"]


@admin.register(Storehouse)
class StorehouseAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "order",
        "reference",
        "storehouse_billings",
        "total_amount",
        "billing_starts",
    ]

    list_filter = ["billing_starts", "paid_at", "created_at"]

    search_fields = ["user", "order", "reference"]


@admin.register(ShippingRate)
class ShippingRateAdmin(admin.ModelAdmin):
    list_display = [
        "state",
        "shipping_fee",
        "updated_at",
    ]

    search_fields = ["state", "shipping_fee"]
    # list_filter = ["state", "paid_at", "created_at"]


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ["percentage_off", "coupon_code"]
    list_filter = ["percentage_off", "is_used", "created_on"]
    search_fields = ["percentage_off", "coupon_code", "is_used"]
