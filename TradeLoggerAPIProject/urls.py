"""TradeLoggerAPIProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="TradeLogger API",
      default_version='v1',
      description="NOTE: A client-side web application consuming these endpoints is currently under development.\n\n"
                  "PROJECT SUMMARY \n\n"
                  "TradeLogger API exposes a number of endpoints that allow traders to log and analyze their trades in "
                  "order to improve future trading performance. The primary motivation for this project is to allow "
                  "myself as well as fellow traders to make more informed (primarily options) trading decisions "
                  "by learning from past successes and mistakes.\n\n"
                  "CONFIGURATION STEPS \n\n"
                  "1. Register a new TradeLogger User using the /auth/register endpoint. \n"
                  "2. Upon successful registration, log in using the /auth/login endpoint. \n"
                  "3. Upon successful login, copy the Authorization response header "
                  "(including the \"Bearer\" prefix). \n"
                  "4. In the top right corner of the page, click \"Authorize\", and paste the entire string copied in "
                  "(3) into the \"Value\" field (again, the value pasted should consist of the token plus the "
                  "\"Bearer\" prefix - e.g. \"Bearer someRandomAuthToken\"). \n"
                  "5. You are ready to start testing the rest of the API endpoints."
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # accepts all endpoints of TradeLoggerAPI
    path('tradeloggerapi/', include('TradeLoggerAPI.urls')),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


