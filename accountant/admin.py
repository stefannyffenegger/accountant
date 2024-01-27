from django.contrib import admin
from . import models
#from .models import CustomUser
from accountant.models import ApplicationUser

# Register your models here.
admin.site.register(models.Transaction)
admin.site.register(models.Account)