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


class HotelAddress(AddressMixin):
    hotel = models.ForeignKey(Hotel, related_name="hotel_address", on_delete=models.DO_NOTHING, null=True)


# class HotelRoom(BaseModelMixin):
#     """
#     HotelRoom
#     """
#     PLAN_1 = 1
#     PLAN_2 = 2
#     MEAL_PLAN_CHOICES = ((PLAN_1, "Plan 1"), (PLAN_2, "Plan 2"))
#     meal_plan = models.IntegerField(choices=MEAL_PLAN_CHOICES)
#
#     def __str__(self):
#         return "HotelId: " + str(self.id)
