from django.db import models


# # Create your models here.
class BaseModelMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    # created_by = models.IntegerField()
    # modified_by = models.IntegerField()
    deleted = models.BooleanField(default=False)


class DetailMixin(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=50, null=True)
    mail = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=12, null=True)
    active = models.BooleanField(default=True)

