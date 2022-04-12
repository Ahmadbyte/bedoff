from django.db import models

from accounts.models import DetailMixin
from hotels.models import Hotel


class TimeLineMixin(models.Model):
    class Meta:
        abstract = True

    createdOn = models.DateTimeField(auto_now=True, auto_now_add=False)
    lastUpdatedOn = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.CharField(max_length=4)


class Vendor(models.Model):
    name = models.CharField(max_length=50)


class BookingOrder(TimeLineMixin):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    ordered_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    source = models.CharField(max_length=50)


class BookingGroup(TimeLineMixin):
    Status = (
        (1, "In Progress"),
        (2, "Completed"),
        (3, "Closed"),
        (4, "Cancelled"),
    )
    BookingType = ((1, "New Booking"), (2, "Extension"))
    TypeOfBookings = ((1, "HNS"), (2, "Relocation"))
    orderId = models.ForeignKey(BookingOrder, on_delete=models.DO_NOTHING)
    checkIn = models.DateTimeField(auto_now=True, auto_now_add=False)
    checkOut = models.DateTimeField(auto_now=True, auto_now_add=False)
    Hotel = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING)
    PreferredHotels = models.CharField(max_length=50, default="")
    NumberOfRooms = models.IntegerField()
    SuggestedHotelList = models.CharField(max_length=100)
    BookingType = models.IntegerField(choices=BookingType)
    TypeOfBookings = models.IntegerField(choices=TypeOfBookings)
    Status = models.IntegerField(choices=Status, default=1)

    def __str__(self):
        return "Booking Group ID: " + str(self.id)


class Guest(DetailMixin):
    EmployeeTNLID = models.CharField(max_length=100, default="")

    def __str__(self):
        return "Visitor Id: " + str(self.id)


class Booking(TimeLineMixin):
    BookingGroupId = models.ForeignKey(BookingGroup, on_delete=models.CASCADE)
    Visitor = models.ForeignKey(Guest, on_delete=models.CASCADE)

    def __str__(self):
        return "Booking ID: " + str(self.id)


class Voucher(models.Model):
    BookingGroup = models.ForeignKey(BookingGroup, on_delete=models.CASCADE)
    CreatedOn = models.DateTimeField(auto_now=True, auto_now_add=False)
