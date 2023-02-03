from django.contrib import admin

from .models import Inbox

# Register your models here.


@admin.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    list_display = ["user", "subject", "message", "has_been_read", "created_at"]

    list_filter = ["subject", "has_been_read", "created_at"]

    search_fields = ['user', "subject", "message", "has_been_read", "created_at"]

