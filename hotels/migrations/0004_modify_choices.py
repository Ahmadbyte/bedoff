# Generated by Django 3.2.13 on 2022-04-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_add_fields_to_hotels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]