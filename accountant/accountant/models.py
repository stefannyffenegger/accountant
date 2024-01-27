from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    receipt = models.ImageField(upload_to="uploads/receipts/%Y/%m/%d/", blank=True)
    guarantee = models.ImageField(upload_to="uploads/guarantees/%Y/%m/%d/", blank=True)
    tag = models.CharField(max_length=100, blank=True)
    beneficiary = models.CharField(max_length=200)
    benefactor = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)
    transactions = models.ForeignKey(Transaction, on_delete=models.CASCADE, blank=True, null=True) # deletes all transactions of account
    tag = models.CharField(max_length=100, blank=True) #TODO: ref array of Tag, tbd
    owners = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) #TODO: ref array of User
    viewers = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) #TODO: ref array of User
    currency = models.CharField(max_length=100) #TODO: use from currency list or create new model

    def __str__(self):
        return self.name
    
#class AppUser(models.Model):
#    email = models.ForeignKey(User, on_delete=models.CASCADE)
#    created = models.DateTimeField(auto_now_add=True)
#    lastedit = models.DateTimeField(auto_now_add=True)
#    
#    def __str__(self):
#        return self.email