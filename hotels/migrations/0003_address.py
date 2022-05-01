# Generated by Django 3.2.13 on 2022-04-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotels", "0002_hotestaff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hoteladdress",
            name="address1",
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name="hoteladdress",
            name="address2",
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name="hoteladdress",
            name="city",
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name="hoteladdress",
            name="country",
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name="hoteladdress",
            name="map_url",
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="hoteladdress",
            name="name",
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name="hoteladdress",
            name="zip_code",
            field=models.CharField(max_length=12, null=True),
        ),
    ]