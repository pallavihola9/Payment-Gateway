from django.db import models

# Create your models here.
class Coffee(models.Model):
    name=models.CharField(max_length=200)
    amount=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    payment_id=models.CharField(max_length=100)
    paid=models.BooleanField(default=False)
