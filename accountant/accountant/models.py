from django.db import models

class Transaction(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    #receipt
    #guarantee
    tag = models.CharField(max_length=100)
    beneficiary = models.CharField(max_length=200)
    benefactor = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    transactions = models.CharField(max_length=50)
    tag = models.CharField(max_length=100)
    owners = models.CharField(max_length=200)
    currency = models.CharField(max_length=100)

    def __str__(self):
        return self.name