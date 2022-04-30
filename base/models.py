import uuid

from django.conf import settings
from django.db import models


class BaseModelMixin(models.Model):
    """
    BaseModelMixin
        A Base Mixin class to handle all fields common to all classes
    """

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_createdby",
        on_delete=models.DO_NOTHING,
        null=True,
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_modifiedby",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class AddressMixin(BaseModelMixin):
    """
    Address
    """

    name = models.CharField(max_length=1024, null=True)
    address1 = models.CharField(max_length=1024, null=True)
    address2 = models.CharField(max_length=1024, null=True)
    zip_code = models.CharField(max_length=12, null=True)
    city = models.CharField(max_length=1024, null=True)
    state = models.CharField(max_length=1024, null=True)
    country = models.CharField(max_length=30, null=True)
    map_url = models.CharField(max_length=400, null=True)

    class Meta:
        abstract = True
