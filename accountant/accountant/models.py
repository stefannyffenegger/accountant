from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager

class AppUser(AbstractUser):
    username = None # Remove "username"
    email = models.EmailField('email address', unique=True)
    
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []

    objects = BaseUserManager()

    class Meta:
        verbose_name = "application user"
        verbose_name_plural = "application users"
    
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    tag = models.CharField(max_length=100, blank=True) #TODO: ref array of Tag, tbd
    owners = models.ManyToManyField(AppUser) #TODO: ref array of User
    viewers = models.ManyToManyField(AppUser, blank=True, null=True) #TODO: ref array of User
    currency = models.CharField(max_length=100) #TODO: use from currency list or create new model

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    receipt = models.ImageField(upload_to="uploads/receipts/%Y/%m/%d/", blank=True)
    guarantee = models.ImageField(upload_to="uploads/guarantees/%Y/%m/%d/", blank=True)
    tag = models.CharField(max_length=100, blank=True)
    created_by = models.ForeignKey(AppUser, on_delete=models.SET_NULL)
    beneficiary = models.CharField(max_length=200)
    benefactor = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
#class AppUser(models.Model):
#    email = models.ForeignKey(User, on_delete=models.CASCADE)
#    created = models.DateTimeField(auto_now_add=True)
#    lastedit = models.DateTimeField(auto_now_add=True)
#    
#    def __str__(self):
#        return self.email