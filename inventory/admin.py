from django.contrib import admin

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

# Register your models here.


class SubcategoryInline(admin.StackedInline):
    model = Subcategory
    fields = ["name", "description", "slug"]


class LowerSubcategoryInline(admin.StackedInline):
    model = LowerSubcategory
    fields = [
        "name",
        "slug",
        "lowersubcategory_icon",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "category"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["category", "name"]
    inlines = [
        LowerSubcategoryInline,
    ]


@admin.register(LowerSubcategory)
class LowerSubcategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "subcategory"]
    prepopulated_fields = {"slug": ("name",)}


class MediaInline(admin.StackedInline):
    model = Media
    fields = ["product_images", "alt_text", "is_feature"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "category",
        "subcategory",
        "price",
        "is_onFlashsale",
        "slug",
    ]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = [
        "category",
        "subcategory",
        "in_stock",
        "is_onFlashsale",
        "is_active",
    ]

    search_fields = [
        "name",
        "description",
        "category",
        "subcategory",
        "price",
        "slug",
    ]

    inlines = [MediaInline]


class ProductAttributeInline(admin.StackedInline):
    model = ProductAttribute
    fields = ["name"]
    # fields = ['name', 'description', 'slug']


class ProductAttributeValueInline(admin.StackedInline):
    model = ProductAttributeValue
    fields = ["value"]
    # fields = ['name', 'description', 'slug']


admin.site.register(ProductType)


@admin.register(ProductAttribute)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = ["name"]

    inlines = [ProductAttributeValueInline]


admin.site.register(ProductAttributeValue)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ["product", "alt_text", "is_feature"]
    list_filter = ["product"]




@admin.register(FlashsaleCtrl)
class FlashsaleCtrlAdmin(admin.ModelAdmin):
    list_display = ["name", "when"]
    list_filter = ["name", "when"]
