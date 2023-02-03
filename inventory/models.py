import random
import string

from cloudinary.models import CloudinaryField
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from users.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("Category Name"),
        help_text=_("format: required, max_length=100"),
    )

    slug = models.SlugField(
        max_length=100,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("Category URL"),
        help_text=_(
            "format: required, letters, numbers, underscore, or hyphens"
        ),
    )

    description = models.TextField(
        verbose_name=_("Category Description"),
        help_text=_("format: optional"),
        null=True,
        blank=True,
    )

    category_image = CloudinaryField(
        "Category Banner Image",
        overwrite=True,
        format="jpg",
        folder="Category Backgrounds",
    )

    category_nav_image = CloudinaryField(
        "Category Nav Image",
        overwrite=True,
        format="jpg",
        folder="Category Nav Images",
        default="",
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        to_assign = slugify(self.name)

        if Category.objects.filter(slug=to_assign).exists():
            to_assign = to_assign + str(Category.objects.all().count())

        self.slug = to_assign

        super().save(*args, **kwargs)


class Subcategory(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name="Main Category",
        related_name="subcategories",
        on_delete=models.PROTECT,
    )

    name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Subcategory Name"),
        help_text=_("format: required, max_length=100"),
    )

    description = models.TextField(
        verbose_name=_("Subcategory Description"),
        help_text=_("format: optional"),
        null=True,
        blank=True,
        default="",
    )

    slug = models.SlugField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Subcategory URL"),
        help_text=_(
            "format: required, letters, numbers, underscore, or hyphens"
        ),
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = _("Subcategory")
        verbose_name_plural = _("Subcategories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})


class LowerSubcategory(models.Model):
    subcategory = models.ForeignKey(
        Subcategory,
        verbose_name="Main Subcategory",
        related_name="lowersubcategories",
        on_delete=models.PROTECT,
    )

    name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Lower Subcategory Name"),
        help_text=_("format: required, max_length=100"),
    )

    slug = models.SlugField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Lower Subcategory URL"),
        help_text=_(
            "format: required, letters, numbers, underscore, or hyphens"
        ),
    )

    lowersubcategory_icon = CloudinaryField(
        "Lower Subcategory Icon",
        overwrite=True,
        format="png",
        folder="Product Type Icons",
        default="",
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = _("Lower Subcategory")
        verbose_name_plural = _("Lower Subcategories")

    def __str__(self):
        return f"{self.subcategory} {self.name}"

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})


class ProductType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Product Type"),
        help_text=_("format: required, unique, max_length-100"),
    )

    # product_type_icon = CloudinaryField(
    #     "Product Type Icon", overwrite=True, format="png", folder="Product Type Icons", default=""
    # )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    product_type = models.ForeignKey(
        ProductType,
        related_name="product_type_attribute",
        on_delete=models.PROTECT,
    )

    name = models.CharField(
        max_length=100,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Product Attribute Name"),
        help_text=_("format: required, unique, max_length-100"),
    )

    def __str__(self):
        return f"{self.product_type} : {self.name}"


class ProductAttributeValue(models.Model):
    attribute = models.ForeignKey(
        ProductAttribute,
        related_name="product_attribute",
        on_delete=models.PROTECT,
    )

    value = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Product Type Attribute Value"),
        help_text=_("format: required, max_length-255"),
    )

    def __str__(self):
        return f"{self.attribute} : {self.value}"


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name="Category",
        related_name="category",
        on_delete=models.PROTECT,
    )

    subcategory = models.ForeignKey(
        Subcategory,
        verbose_name="Subcategory",
        related_name="subcategory",
        on_delete=models.PROTECT,
    )

    lowersubcategory = models.ForeignKey(
        LowerSubcategory,
        verbose_name="Lower Subcategory",
        related_name="lowersubcategory",
        on_delete=models.PROTECT,
    )

    product_type = models.ForeignKey(
        ProductType, related_name="product_type", on_delete=models.PROTECT
    )

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Product Name"),
        help_text=_("format: required, max=100"),
    )

    slug = models.SlugField(
        max_length=255,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("Product URL"),
        help_text=_(
            "format: required, letters, numbers, underscore, or hyphens"
        ),
    )

    description = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Product Description"),
        help_text=_("format: required"),
    )

    attribute_value = models.ManyToManyField(
        ProductAttributeValue,
        verbose_name="Product Attribute Values",
        related_name="product_attribute_value",
        blank=True,
    )

    flashsale = models.IntegerField(
        unique=False,
        null=False,
        blank=False,
        default=0,
        verbose_name=_("Percentage Off"),
        help_text=_(
            "format: how many percent off the  regular price of product"
        ),
    )

    price = models.IntegerField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Regular Price"),
        help_text=_("format: regular price of product"),
    )

    weight = models.FloatField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("Product Weight"),
        help_text=_("Weight in Kilogram (Kg)"),
    )

    is_onFlashsale = models.BooleanField(
        default=False,
        verbose_name=_("Flashsale"),
        help_text=_("format: true = product is on flashsale"),
    )

    in_stock = models.BooleanField(
        default=True,
        verbose_name=_("product availability"),
        help_text=_("format: true = product is available"),
    )

    is_active = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Product Visibility"),
        help_text=_("format: true = product visible"),
    )

    added_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date product was added"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date product was last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    meta_keywords = models.CharField(
        max_length=255,
        verbose_name=_("SEO Keywords"),
        help_text=_("SEO Keywords separated by comma"),
        null=True,
        blank=True,
    )

    meta_description = models.CharField(
        max_length=255,
        verbose_name=_("Meta Description"),
        help_text=_("content for description meta tag"),
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-added_on", "-is_onFlashsale"]
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})

    @property
    def flashsale_price(self):
        if self.is_onFlashsale:
            discount = (self.flashsale / 100) * self.price

            return int((self.price) - discount)
        else:
            return int(self.price)

    def save(self, *args, **kwargs):
        randomUniques = ""
        randomUniqueNums = random.sample(range(1, len(self.name)), 5)

        if randomUniqueNums:
            for num in randomUniqueNums:
                randomUniques = randomUniques + str(num)
        else:
            print("No unique random numbers")

        self.slug = self.slug + "-" + randomUniques

        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     to_assign = slugify(self.name)
    #     to_assign = str(self.subcategory.slug) + "-" + to_assign
    #     self.slug = to_assign

    #     super().save(*args, **kwargs)


class Media(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name="Product Image",
        related_name="product_images",
    )

    product_images = CloudinaryField(
        "Image", format="jpg", folder="Product Images"
    )

    alt_text = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Alternative Text"),
        help_text=_("format: required, max_length-255"),
    )

    is_feature = models.BooleanField(
        default=False,
        verbose_name=_("Default Image"),
        help_text=_("format: default=false, true = default image"),
    )

    added_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date Added"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return self.product.name


class Stock(models.Model):
    product = models.OneToOneField(
        Product,
        related_name="product_stock",
        on_delete=models.PROTECT,
    )

    last_checked = models.DateTimeField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("inventory stock check date"),
        help_text=_("format: Y-m-d H:M:S, null-true, blank-true"),
    )

    units = models.IntegerField(
        default=0,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("units/qty of stock"),
        help_text=_("format: required, default-0"),
    )

    units_sold = models.IntegerField(
        default=0,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("units sold to date"),
        help_text=_("format: required, default-0"),
    )

    def __str__(self):
        return self.units
        # return f"{self.product.name}, Units: {self.units}, Units Sold: {self.units_sold}"


class FlashsaleCtrl(models.Model):
    name = models.CharField(
        max_length=100,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Flashsale Name"),
        help_text=_("format: required, max_length-100"),
    )

    when = models.DateTimeField()

    is_active = models.BooleanField(
        default=False,
        verbose_name=_("Active Flashsale"),
        help_text=_("format: default=false, true = flashsale is active"),
    )

    def __str__(self):
        return self.name



