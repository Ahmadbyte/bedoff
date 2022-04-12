from rest_framework import serializers


class HotelSerializer(serializers.Serializer):
    def __init__(self):
        pass


class AddressSerializer(serializers.Serializer):
    def __init__(self):
        pass


class HotelFilterSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
