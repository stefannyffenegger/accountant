from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
from . import serializers

#@api_view(['GET', 'POST'])
#def transaction_list(request):
#    transaction = models.Transaction.objects.all()
#    serializer = serializers.TransactionSerializer(transaction)
#    return JsonResponse({'transactions': serializer.data})
#
#@api_view(['GET', 'PUT', 'DELETE'])
#def transaction_detail(request, id):
#    try:
#        transaction = models.Transaction.objects.get(pk=id)
#    except models.Transaction.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#
#    serializer = serializers.TransactionSerializer(transaction)
#    return Response(serializer.data, status=status.HTTP_200_OK)

class TransactionViewSet(viewsets.ModelViewSet):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.AppUser.objects.all()
    serializer_class = serializers.UserSerializer