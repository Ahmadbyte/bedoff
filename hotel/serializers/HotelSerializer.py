from rest_framework_json_api import serializers

from hotel.models import Hotel


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id')
    id = serializers.IntegerField()
