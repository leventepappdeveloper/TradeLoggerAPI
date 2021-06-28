from rest_framework.views import APIView
from ..serializers import UserSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from TradeLoggerAPI.Utils.AuthenticationUtils import *
from TradeLoggerAPI.Swagger.SwaggerSchemas import *
from TradeLoggerAPI.Swagger.SwaggerOperationDescriptions import *

class RegisterUserView(APIView):
    @swagger_auto_schema(operation_description=getRegisterUserOpDesc(), request_body=getRegisterUserSchema())
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginUserView(APIView):
    @swagger_auto_schema(operation_description=getLoginUserOpDesc(), request_body=getLoginUserSchema())
    def post(self, request):
        token = issueJWTToken(request)
        response = Response()
        response["Authorization"] = "Bearer " + token
        return response

class UnregisterUserView(APIView):
    @swagger_auto_schema(operation_description=getUnregisterUserOpDesc())
    def post(self, request):
        payload = validateJWTToken(request)
        try:
            ret = User.objects.filter(id=payload['id']).delete()
        except:
            raise Exception('Failed to unregister user')

        return Response(ret)