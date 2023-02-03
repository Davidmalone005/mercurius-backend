from django.urls import path

from . import views

urlpatterns = [
    path("", views.AddressListAPIView.as_view()),
    path("add/", views.AddAddressAPIView),
    path("<str:pk>/update/", views.UpdateAddressAPIView),
    path("<str:pk>/delete/", views.DeleteAddressAPIView),
    path("<str:id>/", views.AddressDetailAPIView.as_view()),
]
