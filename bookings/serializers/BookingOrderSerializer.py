from rest_framework import serializers

from bookings.models import Vendor


class VendorSerializer(serializers.Serializer):
    class Meta:
        model = Vendor
        fields = ("id", "name")

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)


class BookingOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    vendor = VendorSerializer()
    ordered_on = serializers.DateTimeField()
    source = serializers.CharField()
