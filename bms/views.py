from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import parsers, permissions, status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action , api_view, schema
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Create your views here.
from bms.models import BookingGroup, BookingOrder, Vendor, Booking

# {
#     "BookingFilter":
#         {
#             "Status": 1
#
#         }
#
# }
from bms.serializers import BookingGroupSerializer
from bms.serializers.BookingOrderSerializer import BookingOrderSerializer, VendorSerializer


@api_view(['GET','POST'])
# @schema(CustomAutoSchema())
def view(request):
    if request.method == "POST":
        a = Vendor.objects.all()
        print(a[0].name)
        serializerdata= VendorSerializer(data= a, many=True)
        # print(serializerdata.is_valid())
        # content = JSONRenderer().render(serializerdata.errors)
        # print(content)
        # return Response({"message": "Hello for today! See you tomorrow!"})
        return Response(serializerdata, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)

    # vendor = Vendor(name = "Byjus")
    # vendor.save()
    # order = BookingOrder(vendor = vendor , source = "manual")
    # bookingGroup = BookingGroup(order = order)

    # return Response({"message": "Hello for today! See you tomorrow!"})