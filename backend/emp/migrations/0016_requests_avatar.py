# Generated by Django 3.0.6 on 2020-07-05 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0015_auto_20200704_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='Avatar',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]