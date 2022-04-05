from rest_framework_json_api import serializers

from bms.models import BookingGroup, BookingOrder
from bms.serializers import BookingOrderSerializer
from hotel.serializers import HotelSerializer

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


# class BookingOrderSerializer(serializers.Serializer):
#     class Meta:
#         model = BookingOrder
#         fields = ('id' , 'vendor' , 'ordered_on' , 'source')
#     id = serializers.IntegerField()
#     # vendor=VendorSerializer()
#     ordered_on=serializers.DateTimeField()
#     source=serializers.CharField()
#

class BookingGroupSerializer(serializers.Serializer):
    class Meta:
        model = BookingGroup
        fields = ('id','orderId','checkIn','Hotel','PreferredHotel')

    id = serializers.IntegerField()
    orderId = BookingOrderSerializer.BookingOrderSerializer()
    checkIn = serializers.DateTimeField()
    checkOut = serializers.DateTimeField()
    Hotel = HotelSerializer.HotelSerializer(required=False)
    PreferredHotels = serializers.CharField(max_length=50)
    NumberOfRooms = serializers.IntegerField()
    SuggestedHotelList = serializers.CharField(max_length=100)
    BookingType = serializers.IntegerField()
    TypeOfBookings = serializers.IntegerField()
    Status = serializers.IntegerField()
