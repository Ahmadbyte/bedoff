# Generated by Django 3.2.12 on 2022-04-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinggroup',
            name='status',
        ),
        migrations.AddField(
            model_name='bookinggroup',
            name='PreferredHotels',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='bookinggroup',
            name='Status',
            field=models.IntegerField(choices=[(1, 'In Progress'), (2, 'Completed'), (3, 'Closed'), (4, 'Cancelled')], default=1),
        ),
        migrations.AddField(
            model_name='visitor',
            name='EmployeeTNLID',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bookinggroup',
            name='BookingType',
            field=models.IntegerField(choices=[(1, 'New Booking'), (2, 'Extension')]),
        ),
        migrations.AlterField(
            model_name='bookinggroup',
            name='TypeOfBookings',
            field=models.IntegerField(choices=[(1, 'HNS'), (2, 'Relocation')]),
        ),
    ]