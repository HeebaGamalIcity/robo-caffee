from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from accounts.models import User, ResetPasswordCode
from django.core.mail import send_mail
from django.conf import settings
import random
import string


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    data = {
        "state": True,
        "detail": "OK"
    }

    username = request.data.get("email")
    password = request.data.get("password")
    if username is None or password is None:
        data["state"] = False
        data["detail"] = 'Please provide both username and password'
        return Response(data,
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        data["state"] = False
        data["detail"] = 'Invalid Credentials'
        return Response(data, status=HTTP_400_BAD_REQUEST)
    token, _ = Token.objects.get_or_create(user=user)

    data["data"] = {
        "token": token.key,
        "type": user.user_type,
    }
    return Response(data, status=HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def logout(request):
    data = {
        "state": True,
        "detail": "OK"
    }

    try:
        request.user.auth_token.delete()
        return Response(data=data, status=HTTP_200_OK)
    except Exception as e:
        data["state"] = False
        data["detail"] = str(e)
        return Response(data=data, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny,))
def send_email_password(request):
    data = {
        "state": True,
        "detail": "OK"
    }
    try:
        email = request.data.get("email")
        user = User.objects.get(email=email)
        s = string.ascii_letters
        s += string.digits
        repeated = 1
        code_legnth = 4
        for i in range(30):
            c = ''.join(random.choice(s) for i in range(code_legnth))
            try:
                code_obj = ResetPasswordCode(user=user, code=c)
                code_obj.save()
                send_mail("icity reset password", c, settings.EMAIL_HOST_USER, [email])
                return Response(data=data, status=HTTP_200_OK)
            except:
                repeated += 1
                if repeated % 10 == 0:
                    code_legnth += 1
    except Exception as e:
        data["state"] = False
        data["detail"] = str(e)
        return Response(data=data, status=HTTP_400_BAD_REQUEST)

    data["state"] = False
    data["detail"] = "resend"
    return Response(data=data, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny,))
def reset_password(request):
    data = {
        "state": True,
        "detail": "OK"
    }
    try:
        reset_obj = ResetPasswordCode.objects.get(code=request.data.get('code'), used=False)
        user = User.objects.get(pk=reset_obj.user.pk)
        user.set_password(request.data.get("password"))
        user.save()
        reset_obj.used = True
        reset_obj.save()
        return Response(data=data, status=HTTP_200_OK)
    except:
        data["state"] = False
        data["detail"] = "code not valid"
        return Response(data=data, status=HTTP_400_BAD_REQUEST)
