# Generated by Django 3.0.7 on 2020-08-20 01:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_auto_20200819_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]