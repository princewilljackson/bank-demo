# Generated by Django 4.1.2 on 2022-11-23 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_updateuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateuser',
            name='confirm_transaction_pin',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='updateuser',
            name='transaction_pin',
            field=models.IntegerField(default=0),
        ),
    ]
