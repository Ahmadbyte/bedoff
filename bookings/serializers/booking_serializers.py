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

    guests = GuestModelSerializer(many=False)

    def create(self, validated_data):
        # guests = validated_data.pop("guests")
        #
        # booking_models.Guest.objects.create(**guests)
        # for guest in guests:
        #     booking_models.Guest.objects.create(**guest)
        guests_data = validated_data.pop("guests")
        guests_instance = booking_models.Guest.objects.create(**guests_data)
        return booking_models.Booking.objects.create(guests=guests_instance, **validated_data)


class BookingsModelSerializer(BaseModelSerializer):
    """
    BookingsModelSerializer
    """

    class Meta:
        fields = "__all__"
