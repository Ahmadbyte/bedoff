from django.db import models

from accounts import models as accounts_models
from base.models import BaseModelMixin


class Address(BaseModelMixin):
    name = models.CharField(
        max_length=1024,
    )

    address1 = models.CharField(
        max_length=1024,
    )

    address2 = models.CharField(
        max_length=1024,
    )

    zip_code = models.CharField(
        max_length=12,
    )

    city = models.CharField(
        max_length=1024,
    )

    country = models.CharField(max_length=3)

    map_url = models.CharField(max_length=400)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class Hotel(BaseModelMixin):
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    manager = models.ForeignKey(accounts_models.User, related_name="manager", on_delete=models.DO_NOTHING, null=True)
    receptionist = models.ForeignKey(
        accounts_models.User, related_name="receptionist", on_delete=models.DO_NOTHING, null=True
    )
    general_manager = models.ForeignKey(
        accounts_models.User, related_name="general_manager", on_delete=models.DO_NOTHING, null=True
    )
    owner = models.ForeignKey(accounts_models.User, related_name="owner", on_delete=models.DO_NOTHING, null=True)
    account = models.ForeignKey(accounts_models.UserBankAccount, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return "HotelId: " + str(self.id)


class RoomDetails(models.Model):
    MealPlan = ((1, "Plan 1"), (2, "Plan 2"))
    meal_plan = models.IntegerField(choices=MealPlan)

    def __str__(self):
        return "HotelId: " + str(self.id)
