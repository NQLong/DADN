# Generated by Django 3.2.3 on 2021-06-03 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0009_auto_20210603_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wateringhistory',
            name='water_pump',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='water_of_pump', to='Api.iodevice'),
        ),
    ]