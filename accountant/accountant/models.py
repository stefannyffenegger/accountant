from django.db import models

class Transaction(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    amount = models.FloatField()

    def __str__(self):
        return self.name