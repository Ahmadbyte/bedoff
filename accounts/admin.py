from django.contrib import admin

from .models import BankAccount, HotelStaff, User

# Register your models here.
admin.site.register(HotelStaff)
admin.site.register(User)
admin.site.register(BankAccount)
