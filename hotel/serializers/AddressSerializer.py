from rest_framework_json_api import serializers

from hotel.models import Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('id')
    id = serializers.IntegerField()
