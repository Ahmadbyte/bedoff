from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import parsers, permissions, status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action , api_view, schema
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Create your views here.
from bms.models import BookingGroup, BookingOrder, Vendor


# {
#     "BookingFilter":
#         {
#             "Status": 1
#
#         }
#
# }
from bms.serializers import BookingGroupSerializer


@api_view(['GET','POST'])
# @schema(CustomAutoSchema())
def view(request):
    if request.method == "POST":
        a = BookingGroup.objects.filter(Status = 1)
        print(a)
        serializerdata= BookingGroupSerializer(data=a)
        content = JSONRenderer().render(serializerdata.data)
        print(content)
        return Response(content, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)

    # vendor = Vendor(name = "Byjus")
    # vendor.save()
    # order = BookingOrder(vendor = vendor , source = "manual")
    # bookingGroup = BookingGroup(order = order)

    # return Response({"message": "Hello for today! See you tomorrow!"})