from django.db import transaction
from rest_framework import serializers

from base.serializers import BaseModelSerializer
from bookings import models as booking_models
from hotels import models as hotel_models
from hotels.serializers import hotel_serializers


class GuestModelSerializer(BaseModelSerializer):
    """
    GuestModelSerializer
    """

    class Meta:
        model = booking_models.Guest
        fields = "__all__"


class UpdateBookingModelSerializer(BaseModelSerializer):
    """
    BookingModelSerializer
    """

    class Meta:
        model = booking_models.Booking
        fields = "__all__"


class BookingModelSerializer(BaseModelSerializer):
    """
    BookingModelSerializer
    """

    guests = GuestModelSerializer(many=True)
    booked_hotel = serializers.JSONField(write_only=True)
    hotel = hotel_serializers.HotelModelSerializer(read_only=True)
    guest_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = booking_models.Booking
        fields = "__all__"

    def create(self, validated_data):
        guests = validated_data.pop("guests")
        booked_hotel_uid = validated_data.pop("booked_hotel").get("uid")

        with transaction.atomic():
            hotel_instance = hotel_models.Hotel.objects.filter(uid=booked_hotel_uid).first()
            validated_data.update({"hotel": hotel_instance})
            booking_instance = super().create(validated_data=validated_data)
            guest_list = []
            for guest in guests:
                guest_instance = booking_models.Guest.objects.create(booking=booking_instance, **guest)
                guest_list.append(guest_instance.id)
            booking_instance.guests.set(guest_list)
        return booking_instance
