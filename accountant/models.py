from logging import warning
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import ApplicationUserManager
from django.conf import settings
from rest_framework.authtoken.models import Token as AuthToken


class ApplicationUser(AbstractUser):
    """
    Custom ApplicationUser
    Requires unique email as username field instead of username
    """
    username = None
    email = models.EmailField(_("email address"), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    verification_token = models.CharField(max_length=100, null=True)

    objects = ApplicationUserManager()

    class Meta:
        verbose_name = "application user"
        verbose_name_plural = "application users"

    def __str__(self):
        return self.email


class Token(AuthToken):
    '''
    DEPRICATED, replaced by JWT library
    '''
    token_key = models.CharField(max_length=40, db_index=True, unique=True)
    appuser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="authentication_token",
        on_delete=models.CASCADE,
        #verbose_name="User",
    )


class Vault(models.Model):
    '''
    Vaults act as containers for Accounts
    Can be owned by multiple users
    Can be shared with other users
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owners = models.ManyToManyField(ApplicationUser, related_name="vault_owners")
    viewers = models.ManyToManyField(ApplicationUser, related_name="vault_viewers", blank=True) #TODO: ref array of User
    accounts = models.ManyToManyField("Account", related_name="vault_account", blank=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    '''
    Accounts contain Transactions
    Can be owned by multiple users    
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey("Tag", on_delete=models.SET_NULL, blank=True, null=True) #TODO: tbd if needed here
    owners = models.ManyToManyField(ApplicationUser, related_name="account_owners")
    #viewers = models.ManyToManyField(ApplicationUser, related_name="account_viewers", blank=True)
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
    tag = models.ForeignKey("Tag", on_delete=models.SET_NULL, blank=True, null=True)
    created_by = models.ForeignKey(ApplicationUser, on_delete=models.SET_NULL, null=True)
    beneficiary = models.CharField(max_length=200)
    benefactor = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    '''
    Tags are used for filtering and statistics
    e.g. groceries, vacation, salary
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(ApplicationUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name