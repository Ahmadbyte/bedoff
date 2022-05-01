from django.db import models

from base.models import BaseModelMixin
from hotels.models import Hotel


class Guest(BaseModelMixin):
    employee_id = models.CharField(max_length=100, default="")
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return "Guest Id: " + str(self.id)


class Booking(BaseModelMixin):
    """
    Booking
    """

    NEW = 1
    EXTENDED = 2
    BOOKING_TYPE_CHOICES = (
        (NEW, "New Booking"),
        (EXTENDED, "Extension"),
    )
    booking_type = models.IntegerField(choices=BOOKING_TYPE_CHOICES, default=NEW)

    HNS = 1
    RELOCATION = 2
    BOOKING_STAY_TYPE_CHOICES = (
        (1, "HNS"),
        (2, "Relocation"),
    )
    stay_type = models.IntegerField(choices=BOOKING_STAY_TYPE_CHOICES)

    IN_PROGRESS = 1
    COMPLETED = 2
    CLOSED = 3
    CANCELLED = 4
    BOOKING_STATUS_CHOICES = (
        (IN_PROGRESS, "In Progress"),
        (COMPLETED, "Completed"),
        (CLOSED, "Closed"),
        (CANCELLED, "Cancelled"),
    )
    booking_status = models.IntegerField(choices=BOOKING_STATUS_CHOICES, default=IN_PROGRESS)

    check_in = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    check_out = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    single_occupancy_room_count = models.IntegerField(null=True)
    double_occupancy_room_type = models.IntegerField(null=True)
    guests = models.ManyToManyField(Guest)
    hotel = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    @property
    def guest_count(self):
        return self.guests.all().count()
