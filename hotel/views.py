from django.shortcuts import render
from rest_framework import parsers, permissions, status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action, api_view, schema, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Create your views here.
from hotel.DTO_serializer.req_objects import HotelFilterSerializer
from hotel.models import Hotel
from hotel.serializers.HotelSerializer import HotelSerializer


@api_view(['GET','POST'])
@parser_classes([JSONParser])
def hotels(request):
    if request.method == "POST":
        #add filter logic
        filterSerializer = HotelFilterSerializer(data=request.data)
        if filterSerializer.is_valid():
            bg = Hotel.objects.all()
            # resultSerializerdata = BookingGroupSerializer(a, many=True)
            # content = JSONRenderer().render(resultSerializerdata.data)
            HotelList = []
            # for itr in len(bg):
            #     bgi = BookingGroupRes()
            #     bookingGroupList.append(bgi)

            print(HotelList)
            return Response(HotelList, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)