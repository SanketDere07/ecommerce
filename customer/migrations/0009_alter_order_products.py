# Generated by Django 4.2.4 on 2023-12-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='customer.OrderItem', to='customer.product'),
        ),
    ]
