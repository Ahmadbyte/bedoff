from django.db import models

from accounts.models import HotelStaff, BankAccount
from base.models import BaseModelMixin, DetailMixin


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

    MapLink = models.CharField(max_length=400)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class Hotel(BaseModelMixin, DetailMixin):
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    manager = models.ForeignKey(HotelStaff, related_name='manager', on_delete=models.DO_NOTHING, null=True)
    receptionist = models.ForeignKey(HotelStaff, related_name='receptionist', on_delete=models.DO_NOTHING, null=True)
    general_manager = models.ForeignKey(HotelStaff, related_name='general_manager', on_delete=models.DO_NOTHING, null=True)
    owner = models.ForeignKey(HotelStaff, related_name='owner', on_delete=models.DO_NOTHING, null=True)
    account = models.ForeignKey(BankAccount, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return "HotelId: " + str(self.id)


class RoomDetails(models.Model):
    MealPlan = ((1, "Plan 1"), (2, "Plan 2"))
    meal_plan = models.IntegerField(choices=MealPlan)

    def __str__(self):
        return "HotelId: " + str(self.id)


# Create your models here.
