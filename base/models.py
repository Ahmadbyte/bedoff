from django.conf import settings
from django.db import models


class BaseModelMixin(models.Model):
    """
    BaseModelMixin
        A Base Mixin class to handle all fields common to all classes
    """

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_createdby",
        on_delete=models.DO_NOTHING,
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_modifiedby",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        abstract = True
