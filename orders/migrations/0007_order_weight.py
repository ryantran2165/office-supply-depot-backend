# Generated by Django 3.1.2 on 2020-11-23 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='weight',
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
    ]
