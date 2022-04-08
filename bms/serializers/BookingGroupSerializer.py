from rest_framework_json_api import serializers

from bms.models import BookingGroup, BookingOrder
from bms.serializers import BookingOrderSerializer
from hotel.serializers import HotelSerializer
from login.models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


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
