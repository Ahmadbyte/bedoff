from rest_framework import serializers

class GuestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)


class BookingSerializer(serializers.Serializer):
    guest = GuestSerializer()


class BookingGroupSerializer(serializers.Serializer):
    bookings = BookingSerializer(many = True)
    checkInDate = serializers.DateTimeField()
    checkoutDate = serializers.DateTimeField()



class ResultSerializer(serializers.Serializer):
    bookingGroupList = BookingGroupSerializer(many = True)


class BookingFilterSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    checkInDate = serializers.DateTimeField(required=False)
    checkoutDate = serializers.DateTimeField(required=False)
    noOfDays = serializers.IntegerField(required=False)



