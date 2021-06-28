'''from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from TradeLoggerAPI.Utils.AuthenticationUtils import *
from .models import TradingAccount

# Create your views here.
# extends APIView that has post and get methods
class RegisterView(APIView):
    registerSwaggerSchemaParameters = {'username': openapi.Schema(type=openapi.TYPE_STRING,
                                                              description='Username - MUST BE UNIQUE'),
                                        'email': openapi.Schema(type=openapi.TYPE_STRING,
                                                                description='User Email'),
                                        'password': openapi.Schema(type=openapi.TYPE_STRING,
                                                                   description='User Password')}
    registerSwaggerSchema = openapi.Schema(type=openapi.TYPE_OBJECT, properties=registerSwaggerSchemaParameters)
    registerSwaggerDescription = "Performs TradeLogger User Registration. The provided credentials will be used in " \
                                 "the /auth/login endpoint to authenticate a TradeLogger User. Please follow " \
                                 "the above \"CONFIGURATION STEPS\" in order successfully register and authenticate " \
                                 "a new TradeLogger User."

    @swagger_auto_schema(operation_description=registerSwaggerDescription, request_body=registerSwaggerSchema)
    def post(self, request):
        # serializes the fields that we want to return in the response
        # adds data to database, too?
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    loginSwaggerSchemaParameters = {'username': openapi.Schema(type=openapi.TYPE_STRING,
                                                                description="Username"),
                                    'password': openapi.Schema(type=openapi.TYPE_STRING,
                                                               description="User Password")}
    loginSwaggerSchema = openapi.Schema(type=openapi.TYPE_OBJECT, properties=loginSwaggerSchemaParameters)
    loginSwaggerDescription = "Performs TradeLogger User Authentication. Provide a valid Email-Password combination " \
                              "corresponding to a registered TradeLogger User. Upon successful login, copy and paste " \
                              "the authentication token into the \"Authorize\" value field as described in the " \
                              "\"CONFIGURATION STEPS\" above."

    @swagger_auto_schema(operation_description=loginSwaggerDescription, request_body=loginSwaggerSchema)
    def post(self, request):
        token = issueJWTToken(request)

        # Add Bearer token auth header to response message
        response = Response()
        response["Authorization"] = "Bearer " + token

        return response

class UnregisterView(APIView):
    def post(self, request):
        try:
            # in future iterations, we might want to remove all items corresponding to id from all tables
            payload = validateJWTToken(request)
            ret = User.objects.filter(id=payload['id']).delete()
        except:
            raise Exception('Failed to unregister user')

        return Response(ret)

class UserView(APIView):
    def get(self, request):
        payload = validateJWTToken(request)

        # find User object in the db corresponding to the "id" found
        # in the JWT token (and serialize JSON User object)
        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('Invalid authorization token provided. Unauthenticated!')

        serializer = UserSerializer(user)
        return Response(serializer.data)

class CreateTradingAccountView(APIView):
    tradingAccountSwaggerSchemaParameters = {'trading_account_name': openapi.Schema(type=openapi.TYPE_STRING,
                                                               description=""),
                                            'trading_account_description': openapi.Schema(type=openapi.TYPE_STRING,
                                                               description=""),
                                             'starting_balance': openapi.Schema(type=openapi.TYPE_STRING,
                                                                                           description="")
                                             }

    tradingAccountSwaggerSchema = openapi.Schema(type=openapi.TYPE_OBJECT,
                                                 properties=tradingAccountSwaggerSchemaParameters)


    @swagger_auto_schema(operation_description="description", request_body=tradingAccountSwaggerSchema)
    def post(self, request):
        payload = validateJWTToken(request)

        trading_account_instance = TradingAccount(trading_account_name=request.data['trading_account_name'],
                             trading_account_description=request.data['trading_account_description'],
                             starting_balance=request.data['starting_balance'],
                             current_balance=request.data['starting_balance'],
                             user_id_id=payload['id'])
        trading_account_instance.save()
        return Response("Your trading account has been successfully created")'''
