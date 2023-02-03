from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import APIView, api_view
from rest_framework.request import Request
from rest_framework.response import Response

from users.models import User

from .models import Contact
from .serializers import ContactSerializer


class AllContactsAPIView(generics.ListCreateAPIView):
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer


class SingleContactsAPIView(generics.RetrieveAPIView):
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer
  lookup_field = 'pk'

