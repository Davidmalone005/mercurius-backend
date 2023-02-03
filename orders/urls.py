from django.urls import path

from . import views

urlpatterns = [
    path("storehouse/<str:pk>/", views.StorehouseListAPIView),
    path(
        "storehouse/<str:pk>/<str:pk2>/",
        views.UpdateStorehouseOrderAPIViewAPIView.as_view(),
    ),
    path("shippingrates/", views.AllShippingRatesAPIView.as_view()),
    path(
        "shippingrates/<str:state>/", views.SingleShippingRateAPIView.as_view()
    ),
    path("coupons/", views.AllCouponCodesAPIView.as_view()),
    path("coupons/<str:coupon_code>/", views.SingleCouponCodeAPIView.as_view()),
    path(
        "coupons/<str:coupon_code>/disable/", views.DisableCouponCode.as_view()
    ),
    path("<str:pk>/", views.OrdersListAPIView),
]
