# Generated by Django 3.0.6 on 2020-06-23 22:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_auto_20200624_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='NID',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='National ID must be entered exactly 14 digits.', regex='^(\\d{14})$')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='NID',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='National ID must be entered exactly 14 digits.', regex='^(\\d{14})$')]),
        ),
        migrations.AlterField(
            model_name='existence',
            name='NID',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='National ID must be entered exactly 14 digits.', regex='^(\\d{14})$')]),
        ),
        migrations.AlterField(
            model_name='owner',
            name='NID',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='National ID must be entered exactly 14 digits.', regex='^(\\d{14})$')]),
        ),
        migrations.AlterField(
            model_name='requests',
            name='NID',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='National ID must be entered exactly 14 digits.', regex='^(\\d{14})$')]),
        ),
    ]