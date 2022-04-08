from django.shortcuts import render
from rest_framework import parsers, permissions, status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action , api_view, schema
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Create your views here.
from hotel.models import Hotel
from hotel.serializers.HotelSerializer import HotelSerializer


@api_view(['GET'])
# @schema(CustomAutoSchema())
def hotels(request):
    if request.method == "POST":
        #add filter logic
        a = Hotel.objects.all()
        serializerdata= HotelSerializer(a, many=True)
        content = JSONRenderer().render(serializerdata.data)
        print(content)
        return Response(serializerdata.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)