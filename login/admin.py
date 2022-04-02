from django.contrib import admin
from .models import HotelStaff, HotelAccount , user ,BankAccount

# Register your models here.
admin.site.register(HotelStaff)
admin.site.register(HotelAccount)
admin.site.register(user)
admin.site.register(BankAccount)
