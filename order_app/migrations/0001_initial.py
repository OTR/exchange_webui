# Generated by Django 4.0 on 2022-01-09 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveOrdersRawJSON',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='lookup time')),
                ('hash_field', models.CharField(max_length=32)),
                ('raw_json', models.BinaryField(max_length=32768)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='BestPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_sell', models.DecimalField(decimal_places=8, max_digits=12)),
                ('best_buy', models.DecimalField(decimal_places=8, max_digits=12)),
                ('last_price', models.DecimalField(decimal_places=8, max_digits=12)),
                ('volume_24', models.DecimalField(decimal_places=8, max_digits=14)),
                ('lookup_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='lookup time')),
                ('sell_change', models.IntegerField()),
                ('buy_change', models.IntegerField()),
                ('hash_field', models.CharField(max_length=32)),
                ('raw_json', models.BinaryField(max_length=32768)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='BuyOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=8, max_digits=16)),
                ('date', models.DateTimeField()),
                ('label', models.CharField(max_length=127)),
                ('order_id', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=8, max_digits=16)),
                ('total', models.DecimalField(decimal_places=8, max_digits=16)),
            ],
            options={
                'abstract': False,
                'unique_together': {('amount', 'date', 'label', 'order_id', 'price', 'total')},
            },
        ),
        migrations.CreateModel(
            name='SellOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=8, max_digits=16)),
                ('date', models.DateTimeField()),
                ('label', models.CharField(max_length=127)),
                ('order_id', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=8, max_digits=16)),
                ('total', models.DecimalField(decimal_places=8, max_digits=16)),
            ],
            options={
                'abstract': False,
                'unique_together': {('amount', 'date', 'label', 'order_id', 'price', 'total')},
            },
        ),
        migrations.CreateModel(
            name='OrderBookState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_time', models.DateTimeField(verbose_name='lookup time')),
                ('buy_orders', models.ManyToManyField(to='order_app.BuyOrder')),
                ('sell_orders', models.ManyToManyField(to='order_app.SellOrder')),
            ],
        ),
    ]
