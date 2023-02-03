from rest_framework import serializers

from .models import (
    Category,
    FlashsaleCtrl,
    LowerSubcategory,
    Media,
    Product,
    ProductAttribute,
    ProductAttributeValue,
    ProductType,
    Subcategory,
)


class LowerSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LowerSubcategory
        fields = "__all__"

    subcategory = serializers.StringRelatedField()


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = [
            "id",
            "category",
            "name",
            "description",
            "slug",
            "lowersubcategories",
        ]

    category = serializers.StringRelatedField()
    lowersubcategories = LowerSubcategorySerializer(many=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "category_image",
            "subcategories",
        ]

    subcategories = SubcategorySerializer(many=True)


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = "__all__"

    product_type = serializers.StringRelatedField()
    # product_type = ProductTypeSerializer()


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        fields = ["attribute", "value"]

    attribute = serializers.StringRelatedField()
    # attribute = ProductAttributeSerializer()


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ["product", "product_images", "alt_text", "is_feature"]

    product = serializers.StringRelatedField()


# class StockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Stock
#         fields = ["product", "units", "units_sold"]

#     product = serializers.StringRelatedField()
    # product_type = ProductTypeSerializer()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "subcategory",
            "lowersubcategory",
            "product_type",
            "name",
            "slug",
            "description",
            "price",
            "flashsale_price",
            "flashsale",
            "is_onFlashsale",
            "weight",
            "in_stock",
            "attribute_value",
            "product_images",
        ]

    category = serializers.StringRelatedField()
    # subcategory = serializers.StringRelatedField()
    subcategory = SubcategorySerializer()
    lowersubcategory = LowerSubcategorySerializer()
    # lowersubcategory = serializers.StringRelatedField()
    # product_lowersubcategory = LowerSubcategorySerializer(many=True)
    product_type = ProductTypeSerializer()
    # product_stock = StockSerializer()
    # product_stock = serializers.StringRelatedField()
    attribute_value = ProductAttributeValueSerializer(many=True)
    product_images = ProductImageSerializer(many=True)


class FlashsaleCtrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashsaleCtrl
        fields = ["when"]


