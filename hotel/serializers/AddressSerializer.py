from rest_framework_json_api import serializers

from hotel.models import Address


class AddressSerializer(serializers.Serializer):
    class Meta:
        model = Address
        fields = ('id')
    id = serializers.IntegerField()
