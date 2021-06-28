from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from TradeLoggerAPI.Utils.AuthenticationUtils import *
from TradeLoggerAPI.Swagger.SwaggerSchemas import *
from TradeLoggerAPI.Swagger.SwaggerOperationDescriptions import *
from ..serializers import *

'''
Handles requests to the 'tradeloggerapi/tradingaccount/createtradingaccount' HTTP endpoint.
Adds a new entry to the TradingAccount database table.
'''
class CreateTradingAccountView(APIView):
    @swagger_auto_schema(operation_description=getCreateTradingAccountOpDesc(),
                            request_body=getCreateTradingAccountSchema())
    def post(self, request):
        payload = validateJWTToken(request)

        trading_account = TradingAccount.objects.filter(
            user_id=payload['id'],
            trading_account_name=request.data['trading_account_name'])
        if len(trading_account) != 0:
            raise Exception("This user already has a trading account with the same name. Try a different trading"
                            "account name")

        try:
            trading_account_instance = TradingAccount(trading_account_name=request.data['trading_account_name'],
                                                      trading_account_description=request.data[
                                                          'trading_account_description'],
                                                      starting_balance=request.data['starting_balance'],
                                                      current_balance=request.data['starting_balance'],
                                                      user_id=payload['id'])
            trading_account_instance.save()
            return Response("Your trading account has been successfully created")

        except:
            raise Exception('Failed to create trading account')

'''
Handles requests to the 'tradeloggerapi/tradingaccount/deletetradingaccount' HTTP endpoint.
Removes the entry corresponding to the trading account name provided.
'''
class DeleteTradingAccountView(APIView):
    @swagger_auto_schema(operation_description=getDeleteTradingAccountOpDesc(),
                            request_body=getDeleteTradingAccountSchema())
    def post(self, request):
        payload = validateJWTToken(request)
        try:
            TradingAccount.objects.filter(user_id=payload['id'],
                                            trading_account_name=request.data['trading_account_name']).delete()
            return Response("Your trading account has been successfully deleted")
        except:
            raise Exception('Failed to delete the trading account')

'''
Handles requests to the 'tradeloggerapi/tradingaccount/gettradingaccountinfo' HTTP endpoint.
Gets info on the given trading account.
'''
class GetTradingAccountInfoView(APIView):
    @swagger_auto_schema(operation_description=getGetTradingAccountInfoOpDesc(),
                            manual_parameters=[getGetTradingAccountInfoSchema()])
    def get(self, request):
        payload = validateJWTToken(request)
        trading_account = TradingAccount.objects.filter(user_id=payload['id'],
                                                    trading_account_name=request.query_params['trading_account_name'])
        if len(trading_account) == 0:
            raise Exception("There is no trading account with the given name corresponding to this user")

        try:
            serializer = TradingAccountSerializer(data=trading_account[0].__dict__)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)
        except:
            raise Exception("Failed to retrieve information on the given trading account.")