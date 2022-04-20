from rest_framework import serializers

from base.serializers import BaseModelSerializer
from bookings import models as booking_models


class GuestModelSerializer(BaseModelSerializer):
    """
    GuestModelSerializer
    """

    class Meta:
        model = booking_models.Guest
        fields = ['id','name', 'employee_TNLID','booking_id']

    booking_id = serializers.IntegerField(required=False)


class BookingModelSerializer(BaseModelSerializer):
    """
    BookingModelSerializer
    """

    class Meta:
        model = booking_models.Booking
        fields = ['preferred_hotels', 'booking_type', 'type_of_booking', 'status', 'room_count_single_occupancy', \
                  'room_count_double_occupancy', 'guest_count', 'guests']

    guests = GuestModelSerializer(many=True)

    def get_guest_count(self, obj):
        return 123

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
        #
        # booking_models.Guest.objects.create(**guests)
        # booking_group_id = validated_data.pop("booking_order_id")
        booking_instance = booking_models.Booking.objects.create(**validated_data)
        guest_list = []
        for guest in guests:
            guest_instance = booking_models.Guest.objects.create(booking_id=booking_instance.id, **guest)
            guest_list.append(guest_instance.id)
        # guests_data = validated_data.pop("guests")
        # guests_instance = booking_models.Guest.objects.create(**guests_data)
        # return booking_models.Booking.objects.create(guests=guests_instance, **validated_data)
        booking_instance.guests.set(guest_list)
        return booking_instance

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        # instance.title = validated_data.get('title', instance.title)
        # instance.code = validated_data.get('code', instance.code)
        # instance.linenos = validated_data.get('linenos', instance.linenos)
        # instance.language = validated_data.get('language', instance.language)
        # instance.style = validated_data.get('style', instance.style)
        # instance.save()
        return instance


class BookingsModelSerializer(BaseModelSerializer):
    """
    BookingsModelSerializer
    """

    class Meta:
        fields = "__all__"
