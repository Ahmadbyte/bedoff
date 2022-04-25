from django.db import transaction

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
        model = account_models.UserBankAccount
        fields = "__all__"


class UserModelSerializer(BaseModelSerializer):
    """
    HotelStaffModelSerializer
    """

    class Meta:
        model = account_models.User
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
    manager = UserModelSerializer(many=False)
    receptionist = UserModelSerializer(many=False)
    general_manager = UserModelSerializer(many=False)
    owner = UserModelSerializer(many=False)
    account = BankAccountModelSerializer(many=False)

    def create(self, validated_data):
        """
        create
        """
        with transaction.atomic():
            address_data = validated_data.pop("address")
            address_instance = hotel_models.Address.objects.create(**address_data)

            manager_data = validated_data.pop("manager")
            manager_instance = account_models.User.objects.create(**manager_data)

            receptionist_data = validated_data.pop("receptionist")
            receptionist_instance = account_models.User.objects.create(**receptionist_data)

            general_manager_data = validated_data.pop("general_manager")
            general_manager_instance = account_models.User.objects.create(**general_manager_data)

            owner_data = validated_data.pop("owner")
            owner_instance = account_models.User.objects.create(**owner_data)

            account_data = validated_data.pop("account")
            account_instance = account_models.User.objects.create(**account_data)

            return hotel_models.Hotel.objects.create(
                owner=owner_instance,
                receptionist=receptionist_instance,
                general_manager=general_manager_instance,
                account=account_instance,
                manager=manager_instance,
                address=address_instance,
                **validated_data
            )
