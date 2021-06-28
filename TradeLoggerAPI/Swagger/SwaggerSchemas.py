from drf_yasg import openapi

def getRegisterUserSchema():
    registerSwaggerSchemaParameters = {'username': openapi.Schema(type=openapi.TYPE_STRING,
                                                                  description='Username you wish to use for '
                                                                              'future authentication.'),
                                       'email': openapi.Schema(type=openapi.TYPE_STRING,
                                                               description='Your email address.'),
                                       'password': openapi.Schema(type=openapi.TYPE_STRING,
                                                                  description='Password you wish to use for '
                                                                              'future authentication.')}
    registerSwaggerSchema = openapi.Schema(type=openapi.TYPE_OBJECT, properties=registerSwaggerSchemaParameters)
    return registerSwaggerSchema

def getLoginUserSchema():
    loginSwaggerSchemaParameters = {'username': openapi.Schema(type=openapi.TYPE_STRING,
                                                               description="A registered user's username."),
                                    'password': openapi.Schema(type=openapi.TYPE_STRING,
                                                               description="The registered user's password.")}
    loginSwaggerSchema = openapi.Schema(type=openapi.TYPE_OBJECT, properties=loginSwaggerSchemaParameters)
    return loginSwaggerSchema


def getCreateTradingAccountSchema():
    createTradingAccountSwaggerSchemaParameters = {
        'trading_account_name': openapi.Schema(type=openapi.TYPE_STRING,
                                               description="One user cannot have two trading accounts with the "
                                                           "same name."),
        'trading_account_description': openapi.Schema(type=openapi.TYPE_STRING,
                                                      description="Briefly describe the goal of the trading account."),
        'starting_balance': openapi.Schema(type=openapi.TYPE_NUMBER,
                                           description="Starting account balance. Must be a number of at most 15 "
                                                       "digits and at most 2 decimal places.")}

    createTradingAccountSwaggerSchema = openapi.Schema(type=openapi.TYPE_OBJECT,
                                                       properties=createTradingAccountSwaggerSchemaParameters)
    return createTradingAccountSwaggerSchema

def getDeleteTradingAccountSchema():
    deleteTradingAccountSwaggerSchemaParameters = {
        'trading_account_name': openapi.Schema(type=openapi.TYPE_STRING,
                                                description="Must be an existing trading account of the "
                                                            "authenticated user.")
                                                   }

    deleteTradingAccountSwaggerSchema = openapi.Schema(type=openapi.TYPE_OBJECT,
                                                       properties=deleteTradingAccountSwaggerSchemaParameters)
    return deleteTradingAccountSwaggerSchema

def getGetTradingAccountInfoSchema():
    username_param = openapi.Parameter('trading_account_name', in_=openapi.IN_QUERY,
                                       description='Name of the trading account we want to get info on.',
                                       type=openapi.TYPE_STRING)
    return username_param

def getOpenShortIronCondorTradeSchema():
    openIronCondorTradeSwaggerSchemaParameters = {
        'trading_account_name': openapi.Schema(type=openapi.TYPE_STRING,
                                               description="Name of the trading account."),
        'underlying_symbol': openapi.Schema(type=openapi.TYPE_STRING,
                                            description="Stock symbol."),
        'underlying_price': openapi.Schema(type=openapi.TYPE_NUMBER,
                                           description="Stock price."),
        'short_call_strike': openapi.Schema(type=openapi.TYPE_NUMBER,
                                          description="Strike price of the short call option."),
        'short_call_delta': openapi.Schema(type=openapi.TYPE_NUMBER,
                                            description="Delta of the short call option."),
        'long_call_strike': openapi.Schema(type=openapi.TYPE_NUMBER,
                                         description="Strike price of the long call option."),
        'long_call_delta': openapi.Schema(type=openapi.TYPE_NUMBER,
                                           description="Delta of the long call option."),
        'short_put_strike': openapi.Schema(type=openapi.TYPE_NUMBER,
                                         description="Strike price of the short put option."),
        'short_put_delta': openapi.Schema(type=openapi.TYPE_NUMBER,
                                          description="Delta of the short put option."),
        'long_put_strike': openapi.Schema(type=openapi.TYPE_NUMBER,
                                        description="Strike price of the long put option."),
        'long_put_delta': openapi.Schema(type=openapi.TYPE_NUMBER,
                                        description="Delta of the long put option."),
        'position_bid_price': openapi.Schema(type=openapi.TYPE_NUMBER,
                                                description="Bid price of the iron condor position."),
        'position_ask_price': openapi.Schema(type=openapi.TYPE_NUMBER,
                                                description="Ask price of the iron condor position."),
        'open_credit_received_per_contract': openapi.Schema(type=openapi.TYPE_NUMBER,
                                                            description="Credit received per contract."),
        'opening_position_delta': openapi.Schema(type=openapi.TYPE_NUMBER,
                                        description="Position delta."),
        'opening_iv': openapi.Schema(type=openapi.TYPE_NUMBER,
                                     description="Implied volatility. (%)"),
        'annual_low_iv': openapi.Schema(type=openapi.TYPE_NUMBER,
                                        description="52-week low IV. (%)"),
        'annual_high_iv': openapi.Schema(type=openapi.TYPE_NUMBER,
                                         description="52-week high IV. (%)"),
        'opening_iv_range_60_days': openapi.Schema(type=openapi.TYPE_NUMBER,
                                                   description="IV percentile of the 60-day ATM option. (%)"),
        'opening_theta': openapi.Schema(type=openapi.TYPE_NUMBER,
                                        description="Position theta. (YYYY-MM-DD)"),
        'trade_open_date': openapi.Schema(type=openapi.TYPE_STRING,
                                          description="Trade open date. (YYYY-MM-DD)"),
        'date_of_expiration': openapi.Schema(type=openapi.TYPE_STRING,
                                             description="Options expiration date. (YYYY-MM-DD)"),
        'max_profit_probability': openapi.Schema(type=openapi.TYPE_NUMBER,
                                                 description="Probability of maximum profit. (0-1)"),
        'max_loss_probability': openapi.Schema(type=openapi.TYPE_NUMBER,
                                               description="Probability of maximum loss. (0-1)"),
        'profit_probability': openapi.Schema(type=openapi.TYPE_NUMBER,
                                             description="Probability of any profit. (0-1)"),
        'notes': openapi.Schema(type=openapi.TYPE_STRING,
                                             description="Any comments you have on this trade."),
        }

    openIronCondorTradeSwaggerSchema = openapi.Schema(type=openapi.TYPE_OBJECT,
                                                      properties=openIronCondorTradeSwaggerSchemaParameters)
    return openIronCondorTradeSwaggerSchema