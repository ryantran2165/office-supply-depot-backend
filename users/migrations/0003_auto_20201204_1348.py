# Generated by Django 3.1.2 on 2020-12-04 21:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201118_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator(regex='[a-zA-z]+')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator(regex='[a-zA-z]+')]),
        ),
    ]
