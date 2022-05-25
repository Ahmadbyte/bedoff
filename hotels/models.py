from django.db import models

from base.models import AddressMixin, BaseModelMixin


class HotelStaff(BaseModelMixin):
    """
    HotelStaff
    """

    first_name = models.CharField(max_length=128, null=True)
    middle_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    RECEPTIONIST = 4
    MANAGER = 3
    OWNER = 1
    GENERAL_MANAGER = 2

    STAFF_TYPE_CHOICES = (
        (
            RECEPTIONIST,
            "Receptionist",
        ),
        (
            MANAGER,
            "Manager",
        ),
        (
            OWNER,
            "Owner",
        ),
        (
            GENERAL_MANAGER,
            "General Manager",
        ),
    )
    staff_type = models.PositiveSmallIntegerField(default=OWNER, choices=STAFF_TYPE_CHOICES)


class Hotel(BaseModelMixin):
    name = models.CharField(max_length=128, unique=True)
    manager = models.ForeignKey(HotelStaff, related_name="manager_hotels", on_delete=models.DO_NOTHING, null=True)
    receptionist = models.ForeignKey(
        HotelStaff, related_name="receptionist_hotels", on_delete=models.DO_NOTHING, null=True
    )
    general_manager = models.ForeignKey(
        HotelStaff, related_name="general_manager_hotels", on_delete=models.DO_NOTHING, null=True
    )
    owner = models.ForeignKey(HotelStaff, related_name="owner_hotels", on_delete=models.DO_NOTHING, null=True)
    tariff_double_occupancy = models.IntegerField(null=True)
    tariff_single_occupancy = models.IntegerField(null=True)
    email = models.CharField(max_length=128, unique=False, null=True)
    additional_email = models.CharField(max_length=128, unique=False, null=True)


class HotelBankAccount(BaseModelMixin):
    name = models.CharField(max_length=50, null=True)
    ifsc = models.CharField(max_length=50, null=True)
    account_number = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)

    # TODO: Add choices here.
    account_type = models.IntegerField(null=True)
    hotel = models.OneToOneField(Hotel, related_name="hotel_bank_account", on_delete=models.DO_NOTHING, null=True)


class HotelAddress(AddressMixin):
    hotel = models.OneToOneField(Hotel, related_name="hotel_address", on_delete=models.DO_NOTHING, null=True)
