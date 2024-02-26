"""
Authentication/User endpoints:
https://djoser.readthedocs.io/en/latest/base_endpoints.html
JWT endpoints:
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
"""
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from . import models
from . import serializers


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer


class VaultViewSet(viewsets.ModelViewSet):
    queryset = models.Vault.objects.all()
    serializer_class = serializers.VaultSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer

