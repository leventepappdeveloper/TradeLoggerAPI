from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

# needs to be associated with a User!!!
class TradingAccount(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    trading_account_name = models.CharField(max_length=255)
    trading_account_description = models.TextField()
    starting_balance = models.DecimalField(max_digits=15, decimal_places=2)
    current_balance = models.DecimalField(max_digits=15, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)