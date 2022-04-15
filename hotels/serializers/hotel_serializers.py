import accounts.models as account_models
from base.serializers import BaseModelSerializer
from hotels import models as hotel_models


class AddressModelSerializer(BaseModelSerializer):
    """
    AddressModelSerializer
    """

    class Meta:
        model = hotel_models.Address
        fields = "__all__"


class HotelStaffModelSerializer(BaseModelSerializer):
    """
    HotelStaffModelSerializer
    """

    class Meta:
        model = account_models.HotelStaff
        fields = "__all__"


class HotelModelSerializer(BaseModelSerializer):
    """
    HotelModelSerializer
    """

    class Meta:
        model = hotel_models.Hotel
        fields = "__all__"

    address = AddressModelSerializer(many=False)
    manager = HotelStaffModelSerializer(many=False)

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        address_instance = hotel_models.Address.objects.create(**address_data)
        manager_data = validated_data.pop("manager")
        manager_instance = account_models.HotelStaff.objects.create(**manager_data)
        return hotel_models.Hotel.objects.create(manager=manager_instance, address=address_instance, **validated_data)
