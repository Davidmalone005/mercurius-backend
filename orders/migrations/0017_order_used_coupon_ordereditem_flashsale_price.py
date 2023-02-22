# Generated by Django 4.1.3 on 2023-02-22 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0016_alter_coupon_is_used"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="used_coupon",
            field=models.BooleanField(
                default=False, verbose_name="Was coupon applied at Checkout?"
            ),
        ),
        migrations.AddField(
            model_name="ordereditem",
            name="flashsale_price",
            field=models.IntegerField(
                default=0,
                help_text="format: flashsale price of item ordered",
                verbose_name="Ordered Item Flashsale Price",
            ),
            preserve_default=False,
        ),
    ]
