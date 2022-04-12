from django.contrib import admin

# Register your models here.
from hotels.models import Address, Hotel

admin.site.register(Hotel)
admin.site.register(Address)
