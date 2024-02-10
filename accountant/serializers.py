from rest_framework import serializers
#from dj_rest_auth.registration.serializers import RegisterSerializer
from . import models


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = '__all__' #['id', 'name', 'description', 'created', 'amount', 'tag', 'beneficiary', 'benefactor']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'


class VaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vault
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    #TODO: restrict fields if possible
    class Meta:
        model = models.ApplicationUser
        fields = '__all__'


#class UserRegistrationSerializer(RegisterSerializer):
#    '''
#    DEPRICATED, replaced by dj-rest-auth library
#    '''
#    email = serializers.EmailField()
#    #password = serializers.CharField(write_only=True)
#
#    class Meta:
#        model = models.ApplicationUser
#        fields = '__all__'