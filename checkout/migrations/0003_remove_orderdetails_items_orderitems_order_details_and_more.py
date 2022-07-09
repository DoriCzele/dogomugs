# Generated by Django 4.0.5 on 2022-06-27 18:24

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_shippingaddress_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='items',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='order_details',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='checkout.orderdetails'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='created',
            field=models.DateTimeField(
                auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='updated',
            field=models.DateTimeField(
                auto_now=True),
        ),
    ]
