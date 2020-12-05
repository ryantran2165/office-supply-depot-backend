# Generated by Django 3.1.2 on 2020-12-04 22:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20201204_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator(regex='^[ -~]{6,}$')]),
        ),
    ]