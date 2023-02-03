from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.contrib.auth import get_user_model


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    # DRF API View

    return Response({"Mercurius": "Welcome to our API home"}, status=200)
