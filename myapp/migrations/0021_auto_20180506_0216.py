# Generated by Django 2.0.1 on 2018-05-05 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_buy'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='account_number',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='bank_name',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
    ]
