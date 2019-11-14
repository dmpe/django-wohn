# Generated by Django 2.2.6 on 2019-11-02 21:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('core', '0002_auto_20191102_2035'), ('core', '0003_auto_20191102_2157')]

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='apartment_floor',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apartment',
            name='property_address_city_town',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='property_address_street',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='property_address_zipcode',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)]),
        ),
        migrations.AddField(
            model_name='apartment',
            name='property_furnished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartment',
            name='property_garage',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='house',
            name='property_address_city_town',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='property_address_street',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='property_address_zipcode',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)]),
        ),
        migrations.AddField(
            model_name='house',
            name='property_furnished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='house',
            name='property_garage',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='apartment_floor',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='property_address_city_town',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='property_address_street',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='property_address_zipcode',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)]),
        ),
        migrations.AddField(
            model_name='room',
            name='property_furnished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='property_garage',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apartment',
            name='property_status',
            field=models.CharField(choices=[('N', 'New'), ('G', 'Good'), ('UC', 'Under Construction')], default='G', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='property_wash_machine',
            field=models.CharField(choices=[('O', 'Owned'), ('S', 'Shared in house'), ('NP', 'Not present')], default='NP', max_length=2),
        ),
        migrations.AddField(
            model_name='house',
            name='property_status',
            field=models.CharField(choices=[('N', 'New'), ('G', 'Good'), ('UC', 'Under Construction')], default='G', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='property_wash_machine',
            field=models.CharField(choices=[('O', 'Owned'), ('S', 'Shared in house'), ('NP', 'Not present')], default='NP', max_length=2),
        ),
        migrations.AddField(
            model_name='room',
            name='property_status',
            field=models.CharField(choices=[('N', 'New'), ('G', 'Good'), ('UC', 'Under Construction')], default='G', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='property_wash_machine',
            field=models.CharField(choices=[('O', 'Owned'), ('S', 'Shared in house'), ('NP', 'Not present')], default='NP', max_length=2),
        ),
    ]