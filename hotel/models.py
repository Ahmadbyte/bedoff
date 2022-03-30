from django.db import models

from login.models import Address, DetailMixin


class Hotel(DetailMixin):
    # manager=models.ForeignKey(RoomManager, on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    def __str__(self):
        return "Room No: "+str(self.id)

# Create your models here.
