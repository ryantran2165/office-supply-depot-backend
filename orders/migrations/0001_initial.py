# Generated by Django 3.1.2 on 2020-10-23 22:20

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.JSONField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('delivery_cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('delivery_method', models.CharField(max_length=128)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=5)),
                ('is_delivered', models.BooleanField(default=False)),
                ('date_delivered', models.DateTimeField()),
                ('driver_id', models.IntegerField()),
            ],
        ),
    ]
