from rest_framework_json_api import serializers

from bms.models import Booking
from bms.serializers import BookingOrderSerializer
from hotel.serializers import HotelSerializer


class BookingSerializer(serializers.Serializer):
    class Meta:
        model = Booking
        fields = ('id')