from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from base.models import BaseModelMixin


class User(AbstractUser, PermissionsMixin, BaseModelMixin):
    def __str__(self):
        return "user Id: " + str(self.id)


class UserBankAccount(models.Model):
    name = models.CharField(max_length=50, null=True)
    ifsc = models.CharField(max_length=50, null=True)
    account_number = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    account_type = models.IntegerField(null=True)

    def __str__(self):
        return "Id: " + str(self.id)
