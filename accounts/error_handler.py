from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response


def authentication_exception_handler(exc, context):
    # if isinstance(exc, NotAuthenticated):
    #     print(exc)
    #     data = {
    #         "state": False,
    #         "detail": "Invalid token"
    #     }
    #     return Response(data, status=401)

    # else
    # default case
    data = {
            "state": False,
            "detail": str(exc)
        }
    return Response(data, status=400)

    # return exception_handler(exc, context)