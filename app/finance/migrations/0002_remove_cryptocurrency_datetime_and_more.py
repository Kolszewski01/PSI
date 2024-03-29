# Generated by Django 4.2.7 on 2024-01-03 14:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cryptocurrency',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='cryptocurrency',
            name='rate',
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='CryptocurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('cryptocurrency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='finance.cryptocurrency')),
            ],
        ),
    ]
