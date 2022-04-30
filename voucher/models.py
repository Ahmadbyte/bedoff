from django.db import models

from base.models import BaseModelMixin
from bookings import models as booking_model


class Voucher(BaseModelMixin):
    booking_id = models.ForeignKey(booking_model.Booking, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return "Voucher Id: " + str(self.uid)
