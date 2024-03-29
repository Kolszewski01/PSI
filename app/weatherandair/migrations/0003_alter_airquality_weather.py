# Generated by Django 4.2.7 on 2024-01-10 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weatherandair', '0002_alter_airquality_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airquality',
            name='weather',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='air_quality', to='weatherandair.weather'),
        ),
    ]
