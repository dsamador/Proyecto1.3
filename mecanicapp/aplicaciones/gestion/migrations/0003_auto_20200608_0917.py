# Generated by Django 3.0.7 on 2020-06-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20200606_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='vehiculos', verbose_name='Imagen del vehiculo'),
        ),
        migrations.AlterUniqueTogether(
            name='odometro',
            unique_together=set(),
        ),
    ]
