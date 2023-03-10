from django.contrib import admin

from .models import Address


# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "street_name",
        "lga",
        "state",
    ]

    list_filter = [
        "lga",
        "state",
        "country",
        "is_default",
    ]

    search_fields = [
        "user",
        "street_name",
        "lga",
        "state",
        "country",
        "is_default",
    ]
