from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from TradeLoggerAPI.models import User

jwtSecret = "secret"
jwtHashingAlgorithm = "HS256"

def validateJWTToken(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        raise AuthenticationFailed('No authorization token found. Unauthenticated!')
    try:
        # remove "BEARER " part from token, and get its payload
        token = token[7:]
        payload = jwt.decode(token, jwtSecret, algorithms=[jwtHashingAlgorithm])
        return payload
    except:
        raise AuthenticationFailed('Invalid authorization token provided. Unauthenticated!')

def issueJWTToken(request):
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
    return jwt.encode(payload, jwtSecret, algorithm=jwtHashingAlgorithm)