from django.db import models

# import hotels.models as hotels_models
from base.models import DetailMixin


class HotelStaff(DetailMixin):
    StaffType = (
        ("GM", "General Manager"),
        ("OW", "Owner"),
        ("MN", "Manager"),
        ("RC", "Receptionist"),
    )

    role = models.CharField(max_length=2, choices=StaffType)

    def __str__(self):
        return "staff Id: " + str(self.id)


class User(DetailMixin):
    def __str__(self):
        return "user Id: " + str(self.id)


class BankAccount(models.Model):
    name = models.CharField(max_length=5, null=True)
    IFSC = models.CharField(max_length=50, null=True)
    account_number = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    account_type = models.IntegerField(null=True)

    def __str__(self):
        return "Id: " + str(self.id)
