# Generated by Django 4.1.2 on 2023-01-11 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_alter_internationaltransfer_iban_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationaltransfer',
            name='iban_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='internationaltransfer',
            name='routing_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='internationaltransfer',
            name='to_account',
            field=models.CharField(max_length=150),
        ),
    ]
