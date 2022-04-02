from django.contrib import admin

# Register your models here.
from bms.models import BookingGroup, Booking, BookingOrder, Visitor, Vendor

admin.site.register(BookingGroup)
admin.site.register(Booking)
admin.site.register(BookingOrder)
admin.site.register(Vendor)
admin.site.register(Visitor)
