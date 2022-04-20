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


class BankAccountModelSerializer(BaseModelSerializer):
    """
    BankAccountModelSerializer
    """

    class Meta:
        model = hotel_models.BankAccount
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
        depth = 2
        fields = "__all__"

    address = AddressModelSerializer(many=False)
    manager = HotelStaffModelSerializer(many=False)
    receptionist = HotelStaffModelSerializer(many=False)
    general_manager = HotelStaffModelSerializer(many=False)
    owner = HotelStaffModelSerializer(many=False)
    account = BankAccountModelSerializer(many=False)

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        address_instance = hotel_models.Address.objects.create(**address_data)

        manager_data = validated_data.pop("manager")
        manager_instance = account_models.HotelStaff.objects.create(**manager_data)

        receptionist_data = validated_data.pop("receptionist")
        receptionist_instance = account_models.HotelStaff.objects.create(**receptionist_data)

        general_manager_data = validated_data.pop("general_manager")
        general_manager_instance = account_models.HotelStaff.objects.create(**general_manager_data)

        owner_data = validated_data.pop("owner")
        owner_instance = account_models.HotelStaff.objects.create(**owner_data)

        account_data = validated_data.pop("account")
        account_instance = account_models.BankAccount.objects.create(**account_data)

        return hotel_models.Hotel.objects.create(owner=owner_instance, receptionist=receptionist_instance,
                                                 general_manager=general_manager_instance,account=account_instance,
                                                 manager=manager_instance, address=address_instance, **validated_data)
