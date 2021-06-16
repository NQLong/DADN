# Generated by Django 3.2.3 on 2021-06-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0017_feed_feed_farm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='air_humidity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='air_temperature',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='data_air_id',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='data_ground_id',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='data_relay_id',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='ground_humidity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='is_relay_on',
            field=models.BooleanField(null=True),
        ),
    ]
