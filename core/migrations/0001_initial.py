# Generated by Django 2.1.7 on 2019-03-04 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today', models.DateField(auto_now_add=True, verbose_name="Today's Date")),
                ('OneEurCzk', models.DecimalField(decimal_places=3, max_digits=7, verbose_name='1 EUR - CZK')),
                ('OneEurUsd', models.DecimalField(decimal_places=3, max_digits=7, verbose_name='1 EUR - USD')),
                ('OneUsdCzk', models.DecimalField(decimal_places=3, max_digits=7, verbose_name='1 USD - CZK')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_created', models.DateTimeField(auto_now_add=True)),
                ('property_rooms', models.IntegerField()),
                ('property_size_in_sq_meters', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('property_size_in_sq_foot', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('property_price_in_eur', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('property_price_in_czk', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('property_price_in_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('property_offered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'properties',
            },
        ),
    ]
