import random
import string
from datetime import datetime, timedelta
from django.utils import timezone

from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("Customer"),
        related_name="customer",
        on_delete=models.CASCADE,
    )

    paystack_customer_code = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Paystack Customer Code"),
    )

    transaction_id = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Transaction ID"),
    )

    reference = models.CharField(
        max_length=27,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Transaction Reference"),
    )

    amount = models.IntegerField(
        null=False, blank=False, unique=False, verbose_name=_("Amount Paid")
    )

    shipping_fee = models.IntegerField(
        null=False, blank=False, unique=False, verbose_name=_("Shipping Fee")
    )

    sales_tax = models.IntegerField(
        null=False, blank=False, unique=False, verbose_name=_("Sales Tax")
    )

    #   coupon = models.ManyToManyField(Coupon, blank=True)

    payment_method = models.CharField(
        max_length=27,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Payment Method"),
    )

    payment_type = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Payment Type"),
    )

    storehouse = models.BooleanField(
        default=False, verbose_name="Save to Storehouse"
    )

    currency = models.CharField(
        max_length=27,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Currency"),
    )

    paid_at = models.DateTimeField(verbose_name=_("Paid At"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created At")
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.reference


class OrderedItem(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("Item Owner"),
        related_name="item_owner",
        on_delete=models.CASCADE,
    )

    order = models.ForeignKey(
        Order,
        verbose_name=_("Ordered Items"),
        related_name="ordered_items",
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Ordered Item Name"),
        help_text=_("format: required, max=100"),
    )

    description = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Ordered Item Description"),
        help_text=_("format: required"),
    )

    price = models.IntegerField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Ordered Item Price"),
        help_text=_("format: price of item ordered"),
    )

    qty = models.IntegerField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Quantity"),
        help_text=_("format: quantity of item ordered"),
    )

    size = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Item Size"),
        help_text=_("format: S, M, L, XL, or XXL"),
    )

    defaultImage = models.CharField(
        max_length=2000,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Ordered Item Default Image"),
        help_text=_("format: required, max=100"),
    )

    ordered_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date item was ordered"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date ordered item was last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        ordering = [
            "-ordered_at",
        ]
        verbose_name = _("Ordered Item")
        verbose_name_plural = _("Ordered Items")

    def __str__(self):
        return self.name


class Storehouse(models.Model):
    user = models.ForeignKey(
        User,
        default=1,
        verbose_name=_("Storehouse Owner"),
        related_name="storehouse_owner",
        on_delete=models.CASCADE,
    )

    order = models.ForeignKey(
        Order,
        verbose_name=_("Storehouse Order"),
        related_name="storehouse_order",
        on_delete=models.CASCADE,
    )

    transaction_id = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Transaction ID"),
    )

    reference = models.CharField(
        max_length=27,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Transaction Reference"),
    )

    shipping_fee = models.IntegerField(
        null=True, blank=True, unique=False, verbose_name=_("Shipping Fee")
    )

    sales_tax = models.IntegerField(
        null=True, blank=True, unique=False, verbose_name=_("Sales Tax")
    )

    billing_starts = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Billing Starts On")
    )

    storehouse_billings = models.IntegerField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Storehouse Billings"),
    )

    total_amount = models.IntegerField(
        null=True, blank=True, unique=False, verbose_name=_("Total Amount Paid")
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created At")
    )

    has_been_paid = models.BooleanField(
        default=False, verbose_name="Has Been Paid"
    )

    paid_at = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Paid At")
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Storehouse")
        verbose_name_plural = _("Storehouse")

    def __str__(self):
        return self.order.reference

    def save(self, *args, **kwargs):
        self.billing_starts = timezone.now() + timedelta(minutes=5)
        super().save(*args, **kwargs)


class ShippingRate(models.Model):

    state = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Destination State"),
    )

    shipping_fee = models.IntegerField(
        null=False, blank=False, unique=False, verbose_name=_("Shipping Fee")
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created At")
    )

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated At")
    )

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = _("Shipping Rate")
        verbose_name_plural = _("Shipping Rates")

    def __str__(self):
        return self.state


class Coupon(models.Model):

    percentage_off = models.IntegerField(
        unique=False,
        null=False,
        blank=False,
        default=0,
        verbose_name=_("Percentage Off"),
        help_text=_("format: how many percent off the total price of items"),
    )

    coupon_code = models.CharField(
        max_length=7,
        unique=True,
        null=True,
        blank=True,
        default="",
        verbose_name=_("Coupon Code"),
        help_text=_("format: leave blank"),
    )

    is_used = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Has been used? "),
        help_text=_("format: true = coupon has been used"),
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date coupon was created"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date it was last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        ordering = [
            "-created_on",
        ]
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")

    def __str__(self):
        return self.coupon_code

    def save(self, *args, **kwargs):
        randomUniques = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=7)
        )
        self.coupon_code = randomUniques
        super().save(*args, **kwargs)
