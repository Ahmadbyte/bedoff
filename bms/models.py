from django.db import models

from django.db import models
# from login.models import Customer,RoomManager
from datetime import date

from hotel.models import Hotel

class TimeLineMixin(models.Model):
    class Meta:
        abstract = True

    createdOn = models.DateTimeField(auto_now=True, auto_now_add=False)
    lastUpdatedOn = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.CharField(max_length=4);

class Vendor(models.Model):
    name = models.CharField(max_length=50);

class BookingOrder(TimeLineMixin):
    vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE)
    ordered_on=models.DateTimeField(auto_now=True, auto_now_add=False)
    source=models.CharField(max_length=50)

class BookingGroup(TimeLineMixin):
    orderId=models.ForeignKey(BookingOrder, on_delete=models.CASCADE)
    # user_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    status=models.CharField(max_length=50)
    def __str__(self):
        return "Booking Group ID: "+str(self.id)
    # @property
    # def is_past_due(self):
    #     return date.today()>self.end_day

class Booking(TimeLineMixin):
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    # user_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    checkIn = models.DateField(auto_now=False, auto_now_add=False)
    CheckOut= models.DateField(auto_now=False, auto_now_add=False)
    status = models.BooleanField()
    created_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Booking ID: " + str(self.id)
    # @property
    # def is_past_due(self):
    #     return date.today()>self.end_day


