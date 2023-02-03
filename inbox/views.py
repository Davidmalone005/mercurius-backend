from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import APIView, api_view
from rest_framework.request import Request
from rest_framework.response import Response

from users.models import User

from .models import Inbox
from .serializers import InboxSerializer


@api_view(http_method_names=["GET"])
def AllInboxAPIView(request: Request, pk):
    user = User.objects.get(pk=pk)
    queryset = Inbox.objects.all().filter(user=user).filter(has_been_read=False)
    serializer = InboxSerializer(instance=queryset, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET", "PUT"])
def SingleInboxAPIView(request: Request, pk, pk2):
    user = User.objects.get(pk=pk)
    queryset = Inbox.objects.all().filter(user=user).filter(pk=pk2)
    serializer = InboxSerializer(instance=queryset, many=True)

    if request.method == "PUT":
        print(request.data)

        Inbox.objects.all().filter(pk=request.data["id"]).update(
            has_been_read=True
        )

        return Response(data={"status": "Inbox have been marked read..."}, status=status.HTTP_200_OK)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
