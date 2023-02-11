# Generated by Django 4.1.3 on 2023-01-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_alter_ordereditem_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="storehouse",
            field=models.BooleanField(
                default=False, verbose_name="Save to Storehouse"
            ),
        ),
    ]