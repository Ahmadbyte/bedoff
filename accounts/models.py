from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModelMixin


class User(
    AbstractUser,
    BaseModelMixin,
):
    """
    User
    """

    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_("Designates that this user has all permissions without " "explicitly assigning them."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )


class UserBankAccount(BaseModelMixin):
    name = models.CharField(max_length=50, null=True)
    ifsc = models.CharField(max_length=50, null=True)
    account_number = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    account_type = models.IntegerField(null=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bank_accounts",
    )
