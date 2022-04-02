from django.contrib import admin

# Register your models here.
from hotel.models import Hotel, Address

admin.site.register(Hotel)
admin.site.register(Address)
