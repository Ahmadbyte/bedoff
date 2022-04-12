from rest_framework_json_api import serializers

from hotels.models import Hotel


class HotelSerializer(serializers.Serializer):
    class Meta:
        model = Hotel
        fields = "id"

    id = serializers.IntegerField()
