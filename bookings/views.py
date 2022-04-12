from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# Create your views here.
from bookings.DTO_serializer.req_objects import BookingFilterSerializer
from bookings.models import Booking, BookingOrder, Guest

# {
#     "BookingFilter":
#         {
#             "Status": 1
#
#         }
#
# }
from bookings.serializers.BookingOrderSerializer import BookingOrderSerializer
from bookings.serializers.BookingSerializer import BookingSerializer, GuestSerializer


@api_view(["GET", "POST"])
@parser_classes([JSONParser])
def booking_groups(request):
    if request.method == "POST":
        # add filter logic
        filterSerializer = BookingFilterSerializer(data=request.data)
        if filterSerializer.is_valid():
            # resultSerializerdata = BookingGroupSerializer(a, many=True)
            # content = JSONRenderer().render(resultSerializerdata.data)
            bookingGroupList = []
            # for itr in len(bg):
            #     bgi = BookingGroupRes()
            #     bookingGroupList.append(bgi)

            return Response(bookingGroupList, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def booking(request):
    if request.method == "POST":
        # add filter logic
        a = Booking.objects.all()
        serializerdata = BookingSerializer(a, many=True)
        JSONRenderer().render(serializerdata.data)
        return Response(serializerdata.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def guest(request):
    if request.method == "POST":
        # add filter logic
        a = Guest.objects.all()
        serializerdata = GuestSerializer(a, many=True)
        JSONRenderer().render(serializerdata.data)
        return Response(serializerdata.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def order(request):
    if request.method == "POST":
        # add filter logic
        a = BookingOrder.objects.all()
        serializerdata = BookingOrderSerializer(a, many=True)
        JSONRenderer().render(serializerdata.data)
        return Response(serializerdata.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)
