from rest_framework_json_api import serializers

from bms.models import Booking


class BookingGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ('id')
    id = serializers.IntegerField()
