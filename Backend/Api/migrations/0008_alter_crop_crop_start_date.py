# Generated by Django 3.2.3 on 2021-06-02 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0007_auto_20210603_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='crop_start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]