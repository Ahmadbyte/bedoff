from django.db import transaction
from rest_framework import serializers

from base.serializers import BaseModelSerializer
from bookings import models as booking_models
from hotels import models as hotel_models


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

    guests = GuestModelSerializer(many=True)
    booked_hotel = serializers.CharField()

    class Meta:
        model = booking_models.Booking
        fields = "__all__"

    def create(self, validated_data):
        guests = validated_data.pop("guests")
        booked_hotel = validated_data.pop("hotel").get("uid")
        with transaction.atomic():
            hotel_instance = hotel_models.Hotel.objects.filter(uid=booked_hotel).first()
            booking_instance = booking_models.Booking.objects.create(booked_hotel=hotel_instance, **validated_data)
            guest_list = []
            for guest in guests:
                guest_instance = booking_models.Guest.objects.create(booking_id=booking_instance.id, **guest)
                guest_list.append(guest_instance.id)
            booking_instance.guests.set(guest_list)
        return booking_instance
