from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("fullname", "email", "phone", "gender", "dob", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("fullname", "email", "phone", "gender", "dob", "password1", "password2"),
            },
        ),
    )

    list_display = ("fullname", "email", "phone", "gender", "dob", "is_staff", "last_login")
    list_filter = ("gender", "dob", "is_staff", "is_superuser", "is_active", "groups")
    search_fields = ["email", "fullname", "phone",]
    ordering = ("date_joined",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(User, UserAdmin)
