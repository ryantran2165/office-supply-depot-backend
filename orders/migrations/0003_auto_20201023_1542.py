# Generated by Django 3.1.2 on 2020-10-23 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
    ]