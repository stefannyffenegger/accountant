from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer