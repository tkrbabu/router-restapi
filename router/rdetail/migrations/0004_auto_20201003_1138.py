# Generated by Django 3.0.6 on 2020-10-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdetail', '0003_auto_20201003_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routerdetails',
            name='hostname',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='routerdetails',
            name='loopbackid',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='routerdetails',
            name='sapid',
            field=models.CharField(max_length=18, unique=True),
        ),
    ]
