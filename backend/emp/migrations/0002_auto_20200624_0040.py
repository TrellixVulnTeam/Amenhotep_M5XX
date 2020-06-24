# Generated by Django 3.0.6 on 2020-06-23 22:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='NID',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='National ID must be entered exactly 14 digits.', regex='/^\\s*(\\d\\s*){15}$/')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='NID',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='National ID must be entered exactly 14 digits.', regex='/^\\s*(\\d\\s*){15}$/')]),
        ),
        migrations.AlterField(
            model_name='existence',
            name='NID',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='National ID must be entered exactly 14 digits.', regex='/^\\s*(\\d\\s*){15}$/')]),
        ),
        migrations.AlterField(
            model_name='owner',
            name='NID',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='National ID must be entered exactly 14 digits.', regex='/^\\s*(\\d\\s*){15}$/')]),
        ),
        migrations.AlterField(
            model_name='requests',
            name='NID',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='National ID must be entered exactly 14 digits.', regex='/^\\s*(\\d\\s*){15}$/')]),
        ),
    ]
