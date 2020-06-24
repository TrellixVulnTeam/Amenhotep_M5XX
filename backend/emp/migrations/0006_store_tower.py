# Generated by Django 3.0.6 on 2020-06-24 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0005_flat_tower'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='tower',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tower_store', to='emp.Tower'),
            preserve_default=False,
        ),
    ]
