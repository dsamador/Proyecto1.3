# Generated by Django 3.0.7 on 2020-09-08 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0008_vehiculo_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taller',
            name='correo',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='Correo'),
        ),
    ]
