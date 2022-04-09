from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import parsers, permissions, status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action, api_view, schema, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Create your views here.
from bms.DTO.req_objects import BookingGroupRes
from bms.DTO_serializer.req_objects import BookingFilterSerializer
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
@parser_classes([JSONParser])
def booking_groups(request):
    if request.method == "POST":
        #add filter logic
        filterSerializer = BookingFilterSerializer(data=request.data)
        if filterSerializer.is_valid():
            bg = BookingGroup.objects.get(Status = 1)
            # resultSerializerdata = BookingGroupSerializer(a, many=True)
            # content = JSONRenderer().render(resultSerializerdata.data)
            bookingGroupList = []
            # for itr in len(bg):
            #     bgi = BookingGroupRes()
            #     bookingGroupList.append(bgi)

            print(bookingGroupList)
            return Response(bookingGroupList, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def booking(request):
    if request.method == "POST":
        #add filter logic
        a = Booking.objects.all()
        serializerdata= BookingSerializer(a, many=True)
        content = JSONRenderer().render(serializerdata.data)
        print(content)
        return Response(serializerdata.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def guest(request):
    if request.method == "POST":
        #add filter logic
        a = Guest.objects.all()
        serializerdata= GuestSerializer(a, many=True)
        content = JSONRenderer().render(serializerdata.data)
        print(content)
        return Response(serializerdata.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def order(request):
    if request.method == "POST":
        #add filter logic
        a = BookingOrder.objects.all()
        serializerdata= BookingOrderSerializer(a, many=True)
        content = JSONRenderer().render(serializerdata.data)
        print(content)
        return Response(serializerdata.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


