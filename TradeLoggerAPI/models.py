from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class TradingAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trading_account_name = models.CharField(max_length=255)
    trading_account_description = models.TextField()
    starting_balance = models.DecimalField(max_digits=15, decimal_places=2)
    current_balance = models.DecimalField(max_digits=15, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

class ShortIronCondorTrade(models.Model):
    trading_account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE)
    underlying_symbol = models.CharField(max_length=255)
    underlying_price = models.DecimalField(max_digits=15, decimal_places=2)
    short_call_strike = models.DecimalField(max_digits=15, decimal_places=2)
    short_call_delta = models.DecimalField(max_digits=15, decimal_places=2)
    long_call_strike = models.DecimalField(max_digits=15, decimal_places=2)
    long_call_delta = models.DecimalField(max_digits=15, decimal_places=2)
    short_put_strike = models.DecimalField(max_digits=15, decimal_places=2)
    short_put_delta = models.DecimalField(max_digits=15, decimal_places=2)
    long_put_strike = models.DecimalField(max_digits=15, decimal_places=2)
    long_put_delta = models.DecimalField(max_digits=15, decimal_places=2)
    position_bid_price = models.DecimalField(max_digits=15, decimal_places=2)
    position_ask_price = models.DecimalField(max_digits=15, decimal_places=2)
    open_credit_received_per_contract = models.DecimalField(max_digits=15, decimal_places=2)
    closing_debit_paid_per_contract = models.DecimalField(max_digits=15, decimal_places=2)
    opening_position_delta = models.DecimalField(max_digits=15, decimal_places=2)
    closing_position_delta = models.DecimalField(max_digits=15, decimal_places=2)
    opening_iv = models.DecimalField(max_digits=15, decimal_places=2)
    closing_iv = models.DecimalField(max_digits=15, decimal_places=2)
    annual_low_iv = models.DecimalField(max_digits=15, decimal_places=2)
    annual_high_iv = models.DecimalField(max_digits=15, decimal_places=2)
    opening_iv_range_60_days = models.DecimalField(max_digits=15, decimal_places=2)
    closing_iv_range_60_days = models.DecimalField(max_digits=15, decimal_places=2)
    opening_theta = models.DecimalField(max_digits=15, decimal_places=2)
    closing_theta = models.DecimalField(max_digits=15, decimal_places=2)
    trade_open_date = models.CharField(max_length=255)
    trade_close_date = models.CharField(max_length=255)
    date_of_expiration = models.CharField(max_length=255)
    max_profit_probability = models.DecimalField(max_digits=15, decimal_places=2)
    max_loss_probability = models.DecimalField(max_digits=15, decimal_places=2)
    profit_probability = models.DecimalField(max_digits=15, decimal_places=2)
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
