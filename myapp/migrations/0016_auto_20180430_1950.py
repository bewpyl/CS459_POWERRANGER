# Generated by Django 2.0.2 on 2018-04-30 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20180430_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10)),
                ('concert', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.Concert')),
            ],
        ),
        migrations.AlterField(
            model_name='ticket',
            name='zone',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.Zone'),
        ),
    ]
