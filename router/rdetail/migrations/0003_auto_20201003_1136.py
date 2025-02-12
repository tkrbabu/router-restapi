# Generated by Django 3.0.6 on 2020-10-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdetail', '0002_auto_20201003_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routerdetails',
            name='hostname',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='routerdetails',
            name='loopbackid',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='routerdetails',
            name='sapid',
            field=models.CharField(max_length=18),
        ),
    ]
