from django.db import models

class DetailMixin(models.Model):
    class Meta:
        abstract = True
    name=models.CharField(max_length=5)
    mail=models.CharField(max_length=50)
    phone=models.CharField(max_length=5)

class Address(models.Model):
    name = models.CharField(
        "Full name",
        max_length=1024,
    )

    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )

    city = models.CharField(
        "City",
        max_length=1024,
    )

    country = models.CharField(
        "Country",
        max_length=3
    )

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"


class User(DetailMixin):

    def __str__(self):
        return "user Id: "+str(self.id)


class BankAccount(models.model):
    name = models.CharField(max_length=5)
    IFSC = models.CharField(max_length=50)

    def __str__(self):
        return "Id: "+str(self.id)
