from django.contrib import admin

from .models import BankAccount, HotelAccount, HotelStaff, User

# Register your models here.
admin.site.register(HotelStaff)
admin.site.register(HotelAccount)
admin.site.register(User)
admin.site.register(BankAccount)
