from rest_framework import serializers
from . import models

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = ['id', 'name', 'description', 'created', 'amount', 'tag', 'beneficiary', 'benefactor']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'