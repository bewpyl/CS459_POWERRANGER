# Generated by Django 2.0.2 on 2018-05-08 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_auto_20180506_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
    ]
