# Generated by Django 4.0 on 2022-01-01 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0002_bestpriceltv_buyorder_faucetaddress_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BestPriceLTV',
            new_name='BestPrice',
        ),
    ]
