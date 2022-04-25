from django.http import Http404
from rest_framework import serializers
from rest_framework.response import Response

from base.serializers import BaseModelSerializer
from bookings import models as booking_models
from hotels import models as hotel_models


class GuestModelSerializer(BaseModelSerializer):
    """
    GuestModelSerializer
    """

    class Meta:
        model = booking_models.Guest
        fields = ["id", "name", "employee_TNLID"]

    # booking_id = serializers.IntegerField(required=False)
    def get_object(self, pk):
        try:
            return booking_models.Guest.objects.get(pk=pk)
        except booking_models.Guest.DoesNotExist:
            raise Http404

    def update(self, request, *args, **kwargs):

        instance = self.get_object(request.id)
        serializer = GuestModelSerializer(instance=instance, data=args[0])
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class BookingModelSerializer(BaseModelSerializer):
    """
    BookingModelSerializer
    """

    class Meta:
        model = booking_models.Booking
        depth = 1
        fields = [
            "id",
            "preferred_hotels",
            "booking_type",
            "type_of_booking",
            "status",
            "room_count_single_occupancy",
            "room_count_double_occupancy",
            "guest_count",
            "guests",
            "check_out",
            "check_in",
            "booked_hotel",
        ]

    guests = GuestModelSerializer(many=True)
    booked_hotel = serializers.CharField()

    # def get_guests(self, obj):
    #     queryset = booking_models.Guest.objects.all()
    #
    #     # return queryset.filter(**db_filters).exclude(**db_excludes)
    #     return queryset.filter(booking_id=1)
    # return [{"hey": "sad"}]

    # def get_fields(self):
    #     return {}

    def create(self, validated_data):
        guests = validated_data.pop("guests")
        booked_hotel = validated_data.pop("booked_hotel")
        # import pdb;pdb.set_trace()
        hotel_instance = hotel_models.Hotel.objects.get(pk=booked_hotel)
        #
        # booking_models.Guest.objects.create(**guests)
        # booking_group_id = validated_data.pop("booking_order_id")

        booking_instance = booking_models.Booking.objects.create(booked_hotel=hotel_instance, **validated_data)
        # booking_instance = booking_models.Booking.objects.create(**validated_data)
        guest_list = []
        for guest in guests:
            guest_instance = booking_models.Guest.objects.create(booking_id=booking_instance.id, **guest)
            guest_list.append(guest_instance.id)
        # guests_data = validated_data.pop("guests")
        # guests_instance = booking_models.Guest.objects.create(**guests_data)
        # return booking_models.Booking.objects.create(guests=guests_instance, **validated_data)
        booking_instance.guests.set(guest_list)
        return booking_instance

    def get_object(self, pk):
        try:
            return booking_models.Booking.objects.get(pk=pk)
        except booking_models.Booking.DoesNotExist:
            raise Http404

    def update(self, request, *args, **kwargs):

        instance = self.get_object(request.id)
        # del args[0]['guests']
        # guests = validated_data.pop("guests")
        # import pdb; pdb.set_trace()
        serializer = BookingModelSerializer(instance=instance, data=args[0])
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # --error - nafis
        return Response(serializer.data)


class BookingsModelSerializer(BaseModelSerializer):
    """
    BookingsModelSerializer
    """

    class Meta:
        fields = "__all__"
