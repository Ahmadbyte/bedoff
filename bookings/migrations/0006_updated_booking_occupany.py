# Generated by Django 3.2.13 on 2022-05-05 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0005_updated_date_booking"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="double_occupancy_room_type",
            new_name="double_occupancy_room_count",
        ),
    ]
