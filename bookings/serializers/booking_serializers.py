from base.serializers import BaseModelSerializer
from bookings import models as booking_models


class GuestModelSerializer(BaseModelSerializer):
    """
    GuestModelSerializer
    """

    class Meta:
        model = booking_models.Guest
        fields = "__all__"


class BookingModelSerializer(BaseModelSerializer):
    """
    BookingModelSerializer
    """

    class Meta:
        model = booking_models.Booking
        fields = "__all__"

    guests = GuestModelSerializer(many=True)

    def create(self, validated_data):
        guests = validated_data.pop("guests")

        for guest in guests:
            booking_models.Guest.objects.create(**guest)
        return booking_models.Booking.objects.create(**validated_data)


class BookingsModelSerializer(BaseModelSerializer):
    """
    BookingsModelSerializer
    """

    class Meta:
        fields = "__all__"
