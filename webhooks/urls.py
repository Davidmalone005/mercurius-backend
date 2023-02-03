from django.urls import path

from . import views

urlpatterns = [
    # path("", views.WebhookAPIView),
    path("paystack/", views.PaystackWebhookAPIView),
]
