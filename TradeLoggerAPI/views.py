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
    registerSwaggerSchemaParameters = {'name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
                                        'email': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
                                        'password': openapi.Schema(type=openapi.TYPE_STRING, description='string')}
    registerSwaggerSchema = openapi.Schema(type=openapi.TYPE_OBJECT, properties=registerSwaggerSchemaParameters)

    @swagger_auto_schema(operation_description="description", request_body=registerSwaggerSchema)
    def post(self, request):
        # serializes the fields that we want to return in the response
        # adds data to database, too?
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    loginSwaggerSchemaParameters = {'email': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
                                    'password': openapi.Schema(type=openapi.TYPE_STRING, description='string')}
    loginSwaggerSchema = openapi.Schema(type=openapi.TYPE_OBJECT, properties=loginSwaggerSchemaParameters)

    @swagger_auto_schema(operation_description="description", request_body=loginSwaggerSchema)
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()

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

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'Message': 'success'
        }
        return response
