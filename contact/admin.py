from django.contrib import admin

from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message", "sent_at"]

    list_filter = ["name", "email"]

    search_fields = ["name", "email"]

