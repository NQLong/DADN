# Generated by Django 3.2.3 on 2021-06-16 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0018_auto_20210616_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='data_from_air_sensor',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='data_from_ground_sensor',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='data_from_relay',
        ),
    ]
