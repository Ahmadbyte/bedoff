# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# # Create your views here.
#
#
# @api_view(["GET"])
# # @schema(CustomAutoSchema())
# def view(request):
#     return Response({"message": "Hello for today! See you tomorrow!"})

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        "user": str(request.user),  # `django.contrib.auth.User` instance.
        "auth": str(request.auth),  # None
    }
    return Response(content)
