from django.contrib import admin

# Register your models here.
from bms.models import BookingGroup, Booking, BookingOrder, Vendor, Guest

admin.site.register(BookingGroup)
admin.site.register(Booking)
admin.site.register(BookingOrder)
admin.site.register(Vendor)
admin.site.register(Guest)
