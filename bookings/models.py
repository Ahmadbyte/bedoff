from django.db import models

#
# class TimeLineMixin(models.Model):
#     class Meta:
#         abstract = True
#
#     createdOn = models.DateTimeField(auto_now=True, auto_now_add=False)
#     lastUpdatedOn = models.DateTimeField(auto_now=True, auto_now_add=False)
#     active = models.CharField(max_length=4)
#
#
# class Vendor(models.Model):
#     name = models.CharField(max_length=50)
#
#
# class BookingOrder(TimeLineMixin):
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     ordered_on = models.DateTimeField(auto_now=True, auto_now_add=False)
#     source = models.CharField(max_length=50)


class Guest(models.Model):
    employee_TNLID = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100, default="")
    booking_id = models.IntegerField()

    def __str__(self):
        return "Guest Id: " + str(self.id)


class Booking(models.Model):
    Status = (
        (1, "In Progress"),
        (2, "Completed"),
        (3, "Closed"),
        (4, "Cancelled"),
    )
    BookingType = ((1, "New Booking"), (2, "Extension"))
    TypeOfBookings = ((1, "HNS"), (2, "Relocation"))

    check_in = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    check_out = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    preferred_hotels = models.CharField(max_length=50, default="")
    booking_type = models.IntegerField(choices=BookingType)
    type_of_booking = models.IntegerField(choices=TypeOfBookings)
    status = models.IntegerField(choices=Status, default=1)
    room_count_single_occupancy = models.IntegerField()
    room_count_double_occupancy = models.IntegerField()
    guests = models.ManyToManyField(Guest, null=True)
    guest_count = models.IntegerField()

    def __str__(self):
        return "Booking Group ID: " + str(self.id)


#
# class Booking(TimeLineMixin):
#     BookingGroupId = models.ForeignKey(BookingGroup, on_delete=models.CASCADE)
#     Visitor = models.ForeignKey(Guest, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "Booking ID: " + str(self.id)
#
#
# class Voucher(models.Model):
#     BookingGroup = models.ForeignKey(BookingGroup, on_delete=models.CASCADE)
#     CreatedOn = models.DateTimeField(auto_now=True, auto_now_add=False)
