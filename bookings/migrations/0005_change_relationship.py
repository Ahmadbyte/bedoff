# Generated by Django 3.2.13 on 2022-04-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_change_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='guests',
            field=models.ManyToManyField(null=True, to='bookings.Guest'),
        ),
    ]