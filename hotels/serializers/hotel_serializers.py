from django.db import transaction

from base.serializers import BaseModelSerializer
from hotels import models as hotel_models


class AddressModelSerializer(BaseModelSerializer):
    """
    AddressModelSerializer
    """

    class Meta:
        model = hotel_models.HotelAddress
        fields = "__all__"


class BankAccountModelSerializer(BaseModelSerializer):
    """
    BankAccountModelSerializer
    """

    class Meta:
        model = hotel_models.HotelBankAccount
        fields = "__all__"


class HotelStaffModelSerializer(BaseModelSerializer):
    """
    HotelStaffModelSerializer
    """

    class Meta:
        model = hotel_models.HotelStaff
        fields = "__all__"


class HotelModelSerializer(BaseModelSerializer):
    """
    HotelModelSerializer
    """

    hotel_address = AddressModelSerializer(many=True, read_only=True)
    address = AddressModelSerializer(many=False, write_only=True)
    manager = HotelStaffModelSerializer(many=False)
    receptionist = HotelStaffModelSerializer(many=False)
    general_manager = HotelStaffModelSerializer(many=False)
    owner = HotelStaffModelSerializer(many=False)
    bank_account = BankAccountModelSerializer(many=False, write_only=True)
    hotel_bank_account = BankAccountModelSerializer(many=True, read_only=True)

    class Meta:
        model = hotel_models.Hotel
        fields = '__all__'

    def create(self, validated_data):
        """
        create
        """
        with transaction.atomic():
            address_data = validated_data.pop("address")
            manager_data = validated_data.pop("manager")
            receptionist_data = validated_data.pop("receptionist")
            general_manager_data = validated_data.pop("general_manager")
            owner_data = validated_data.pop("owner")
            bank_account = validated_data.pop("bank_account")

            owner_instance = hotel_models.HotelStaff.objects.create(**owner_data)
            receptionist_instance = hotel_models.HotelStaff.objects.create(**receptionist_data)
            general_manager_instance = hotel_models.HotelStaff.objects.create(**general_manager_data)
            manager_instance = hotel_models.HotelStaff.objects.create(**manager_data)


            validated_data.update(
                {
                    "owner": owner_instance,
                    "manager": manager_instance,
                    "receptionist": receptionist_instance,
                    "general_manager": general_manager_instance,
                }
            )
            hotel_instance = super().create(validated_data=validated_data)
            hotel_models.HotelBankAccount.objects.create(**bank_account, hotel=hotel_instance)
            hotel_models.HotelAddress.objects.create(**address_data, hotel=hotel_instance)

            return hotel_instance
