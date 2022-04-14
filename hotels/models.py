from django.db import models

from accounts.models import HotelStaff


class Address(models.Model):
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


class Hotel(models.Model):
    name = models.CharField(max_length=100, default="")
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    manager = models.ForeignKey(HotelStaff, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return "HotelId: " + str(self.id)


# Create your models here.
