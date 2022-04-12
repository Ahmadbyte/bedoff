from rest_framework_json_api import serializers

from bookings.models import Booking, Guest


class BookingSerializer(serializers.Serializer):
    class Meta:
        model = Booking
        fields = "id"


class GuestSerializer(serializers.Serializer):
    class Meta:
        model = Guest
        fields = "id"
