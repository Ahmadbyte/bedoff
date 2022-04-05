from rest_framework_json_api import serializers

from bms.models import BookingGroup


class BookingGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookingGroup
        fields = ('orderId', 'checkin', 'checkout', 'Status')
    orderId = serializers.IntegerField()
    checkin = serializers.DateTimeField()
    checkout = serializers.DateTimeField()
    Status = serializers.IntegerField()
