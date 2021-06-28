from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from TradeLoggerAPI.Utils.AuthenticationUtils import *
from ..models import *
from TradeLoggerAPI.Swagger.SwaggerOperationDescriptions import *
from TradeLoggerAPI.Swagger.SwaggerSchemas import *

class OpenShortIronCondorView(APIView):
    @swagger_auto_schema(operation_description=getOpenShortIronCondorOpDesc(),
                         request_body=getOpenShortIronCondorTradeSchema())
    def post(self, request):
        payload = validateJWTToken(request)
        trading_account = TradingAccount.objects.filter(user_id=payload['id'],
                                                    trading_account_name=request.data['trading_account_name']).first()

        iron_condor_instance = ShortIronCondorTrade(
                            trading_account_id=trading_account.id,
                            underlying_symbol=request.data['underlying_symbol'],
                            underlying_price=request.data['underlying_price'],
                            short_call_strike=request.data['short_call_strike'],
                            short_call_delta=request.data['short_call_delta'],
                            long_call_strike=request.data['long_call_strike'],
                            long_call_delta=request.data['long_call_delta'],
                            short_put_strike=request.data['short_put_strike'],
                            short_put_delta=request.data['short_put_delta'],
                            long_put_strike=request.data['long_put_strike'],
                            long_put_delta=request.data['long_put_delta'],
                            position_bid_price=request.data['position_bid_price'],
                            position_ask_price=request.data['position_ask_price'],
                            open_credit_received_per_contract=request.data['open_credit_received_per_contract'],
                            closing_debit_paid_per_contract=-1,
                            opening_position_delta=request.data['opening_position_delta'],
                            closing_position_delta=0,
                            opening_iv=request.data['opening_iv'],
                            closing_iv=0,
                            annual_low_iv=request.data['annual_low_iv'],
                            annual_high_iv=request.data['annual_high_iv'],
                            opening_theta=request.data['opening_theta'],
                            closing_theta=0,
                            opening_iv_range_60_days=request.data['opening_iv_range_60_days'],
                            closing_iv_range_60_days=0,
                            trade_open_date=request.data['trade_open_date'],
                            trade_close_date=0,
                            date_of_expiration=request.data['date_of_expiration'],
                            max_profit_probability=request.data['max_profit_probability'],
                            max_loss_probability=request.data['max_loss_probability'],
                            profit_probability=request.data['profit_probability'],
                            notes=request.data['notes'])
        iron_condor_instance.save()
        return Response("Your iron condor trade has been saved successfully")

