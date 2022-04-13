# Generated by Django 3.2.13 on 2022-04-13 20:57
from typing import List

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: List = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=1024, verbose_name="Full name")),
                ("address1", models.CharField(max_length=1024, verbose_name="Address line 1")),
                ("address2", models.CharField(max_length=1024, verbose_name="Address line 2")),
                ("zip_code", models.CharField(max_length=12, verbose_name="ZIP / Postal code")),
                ("city", models.CharField(max_length=1024, verbose_name="City")),
                ("country", models.CharField(max_length=3, verbose_name="Country")),
                ("MapLink", models.CharField(max_length=400)),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresses",
            },
        ),
        migrations.CreateModel(
            name="Hotel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("address", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="hotels.address")),
            ],
        ),
    ]
