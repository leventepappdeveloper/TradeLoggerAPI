from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
import jwt, datetime
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        # Build JWT Token - valid for 60 seconds
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm="HS256")

        # Add Bearer token auth header to response message
        response = Response()
        response["Authorization"] = "Bearer " + token

        return response

class UserView(APIView):
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            raise AuthenticationFailed('No authorization token found. Unauthenticated!')

        try:
            # remove "BEARER " part from token, and get its payload
            token = token[7:]
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except:
            raise AuthenticationFailed('Invalid authorization token provided. Unauthenticated!')

        # find User object in the db corresponding to the "id" found
        # in the JWT token (and serialize JSON User object)
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
