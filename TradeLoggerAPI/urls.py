from django.contrib import admin
from django.urls import path, include
from TradeLoggerAPI.HTTP.TradingAccountViews import *
from TradeLoggerAPI.HTTP.AuthViews import *
from TradeLoggerAPI.HTTP.IronCondorViews import *

urlpatterns = [
    # accepts all endpoints of TradeLoggerAPI
    path('auth/registeruser', RegisterUserView.as_view()),
    path('auth/loginuser', LoginUserView.as_view()),
    path('auth/unregisteruser', UnregisterUserView.as_view()),
    path('tradingaccount/createtradingaccount', CreateTradingAccountView.as_view()),
    path('tradingaccount/deletetradingaccount', DeleteTradingAccountView.as_view()),
    path('tradingaccount/gettradingaccountinfo', GetTradingAccountInfoView.as_view()),
    path('optionstrading/ironcondor/openshortironcondor', OpenShortIronCondorView.as_view()),
]