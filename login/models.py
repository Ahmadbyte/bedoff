from django.db import models

from hotel.models import Hotel


class DetailMixin(models.Model):
    class Meta:
        abstract = True
    name=models.CharField(max_length=5)
    mail=models.CharField(max_length=50)
    phone=models.CharField(max_length=5)
    active= models.BooleanField()


class HotelStaff(DetailMixin):
    StaffTyoe = (
        ('RM', 'Regional Manager'),
        ('OW', 'Owner'),
        ('MN', 'Manager'),
        ('RC', 'Receptionist'),
    )

    role =  models.CharField(max_length=2, choices=StaffTyoe)
    hotel= models.ForeignKey(Hotel,on_delete=models.DO_NOTHING)

    status = models.IntegerField()

    def __str__(self):
        return "staff Id: "+str(self.id)

class user(DetailMixin):

    def __str__(self):
        return "user Id: "+str(self.id)


class BankAccount(models.Model):
    name = models.CharField(max_length=5)
    IFSC = models.CharField(max_length=50)

    def __str__(self):
        return "Id: "+str(self.id)

class HotelAccount(models.Model):
    hotel= models.ForeignKey(Hotel, on_delete=models.CASCADE)
    account = models.ForeignKey(BankAccount ,on_delete=models.CASCADE)

    def __str__(self):
        return "Id: "+str(self.id)
