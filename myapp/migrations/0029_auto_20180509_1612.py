# Generated by Django 2.0.2 on 2018-05-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_remove_customer_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='num_phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
