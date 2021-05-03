from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
import jwt, datetime

# Create your views here.
# extends APIView that has post and get methods
class RegisterView(APIView):
    def post(self, request):
        # serializes the fields that we want to return in the response
        # adds data to database, too?
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()

        response = Response()
        response["Access-Control-Expose-Headers"] = '*'
        token = ''
        response["Authorization"] = "jwt=" + token;

        if user is None:
            #raise AuthenticationFailed('User not found!')
            return response

        if not user.check_password(password):
            #raise AuthenticationFailed('Incorrect password!')
            return response

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        # secret will need to go somewhere else
        token = jwt.encode(payload, 'secret', algorithm="HS256")

        # look into httponly here
        response.set_cookie(key='TradeLoggerAuthCookie', value=token, httponly=True)
        response["Authorization"] = "jwt=" + token

        return response

class UserView(APIView):
    # gets cookie and retrieves user corresponding to token in cookie
    def get(self, request):
        token = request.COOKIES.get('jwt')
        # token cookie to get user
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            # see payload above
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

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
