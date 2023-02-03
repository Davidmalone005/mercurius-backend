from django.contrib import admin
from .models import Webhook

# Register your models here.
class WebhookAdmin(admin.ModelAdmin):
  list_display = ("name", "slug", "description", "created_on")
  list_filter = ("created_on",)
  search_fields = ("name",)
  ordering = ("created_on",)
  prepopulated_fields = {"slug": ("name",)}


admin.site.register(Webhook, WebhookAdmin)
