from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import parsers, permissions, status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action , api_view, schema
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Create your views here.
from bms.models import BookingGroup, BookingOrder, Vendor, Booking, Guest

# {
#     "BookingFilter":
#         {
#             "Status": 1
#
#         }
#
# }
from bms.serializers.BookingGroupSerializer import BookingGroupSerializer
from bms.serializers.BookingOrderSerializer import BookingOrderSerializer
from bms.serializers.BookingSerializer import BookingSerializer, GuestSerializer


@api_view(['GET','POST'])
def booking_groups(request):
    if request.method == "POST":
        #add filter logic
        a = BookingGroup.objects.all()
        serializerdata= BookingGroupSerializer(a, many=True)
        content = JSONRenderer().render(serializerdata.data)
        print(content)
        return Response(serializerdata.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)

def booking(request):
    if request.method == "POST":
        #add filter logic
        a = Booking.objects.all()
        serializerdata= BookingSerializer(a, many=True)
        content = JSONRenderer().render(serializerdata.data)
        print(content)
        return Response(serializerdata.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


def guest(request):
    if request.method == "POST":
        #add filter logic
        a = Guest.objects.all()
        serializerdata= GuestSerializer(a, many=True)
        content = JSONRenderer().render(serializerdata.data)
        print(content)
        return Response(serializerdata.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


def order(request):
    if request.method == "POST":
        #add filter logic
        a = BookingOrder.objects.all()
        serializerdata= BookingOrderSerializer(a, many=True)
        content = JSONRenderer().render(serializerdata.data)
        print(content)
        return Response(serializerdata.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


