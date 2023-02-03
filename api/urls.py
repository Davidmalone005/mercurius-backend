from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

# router = routers.SimpleRouter()
# router.register(r"users", UserViews.UserViewSet)
urlpatterns = [
    path("auth/", obtain_auth_token),
    path("", views.api_home),
    path("addresses/", include("addresses.urls")),
    path("users/", include("users.urls")),
    path("inventory/", include("inventory.urls")),
    path("webhooks/", include("webhooks.urls")),
    path("orders/", include("orders.urls")),
    path("inbox/", include("inbox.urls")),
    path("contact/", include("contact.urls")),
]
# urlpatterns += router.urls
