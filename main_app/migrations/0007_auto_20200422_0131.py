# Generated by Django 3.0.4 on 2020-04-22 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_customer_delivery_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='availability_date',
            field=models.DateField(null=True, verbose_name='available date'),
        ),
    ]
