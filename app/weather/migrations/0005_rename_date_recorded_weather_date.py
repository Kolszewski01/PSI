# Generated by Django 4.2.7 on 2024-01-02 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_alter_airquality_quality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='date_recorded',
            new_name='date',
        ),
    ]
