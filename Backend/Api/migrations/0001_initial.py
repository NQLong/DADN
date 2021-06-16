# Generated by Django 3.2.3 on 2021-06-02 11:13

import Api.models
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_start_date', models.DateTimeField()),
                ('crop_harvest_date', models.DateTimeField()),
                ('crop_state', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_name', models.CharField(default='', max_length=50)),
                ('farm_image', models.ImageField(default='farm_image/default.jpg', upload_to=Api.models.upload_farm_iamge, verbose_name='FarmImage')),
                ('farm_create_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_username', models.CharField(max_length=100)),
                ('feed_key', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_location_index', models.IntegerField()),
                ('area_length', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('area_width', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('field_create_at', models.DateTimeField(default=datetime.datetime.now)),
                ('field_farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields_of_farm', to='Api.farm')),
            ],
        ),
        migrations.CreateModel(
            name='IODevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_feed_name', models.CharField(max_length=50)),
                ('device_type', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)])),
                ('is_my_device', models.BooleanField(default=True)),
                ('device_feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feed_of_device', to='Api.feed')),
                ('device_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='air_sensor_of_field', to='Api.field')),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_name', models.CharField(default='', max_length=50)),
                ('production_image', models.ImageField(default='production_image/default.jpg', upload_to=Api.models.upload_production_iamge, verbose_name='ProductionImage')),
                ('production_period', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WateringHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('watering_start_time', models.DateTimeField()),
                ('watering_end_time', models.DateTimeField()),
                ('Watering_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='water_for_field', to='Api.field')),
                ('water_pump', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='water_of_pump', to='Api.iodevice')),
                ('watering_crop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='water_for_crop', to='Api.crop')),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ground_humidity', models.FloatField()),
                ('air_humidity', models.FloatField()),
                ('air_temperature', models.FloatField()),
                ('record_time', models.DateTimeField()),
                ('data_ground_id', models.CharField(max_length=30)),
                ('data_air_id', models.CharField(max_length=30)),
                ('data_crop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_of_crop', to='Api.crop')),
                ('data_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_of_field', to='Api.field')),
                ('data_from_air_sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='air_sensor', to='Api.iodevice')),
                ('data_from_ground_sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ground_sensor', to='Api.iodevice')),
            ],
        ),
        migrations.AddField(
            model_name='crop',
            name='crop_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crops_of_field', to='Api.field'),
        ),
        migrations.AddField(
            model_name='crop',
            name='crop_production',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production_of_crop', to='Api.production'),
        ),
    ]
