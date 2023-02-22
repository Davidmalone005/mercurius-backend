from django.urls import path

from . import views

urlpatterns = [
    path("paystack/", views.PaystackWebhookAPIView),
    path("paystack/callback/", views.PaystackCallbackUrlAPIView),
]
