# Generated by Django 4.1.3 on 2023-02-01 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0002_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Coupon",
        ),
    ]
