# Generated by Django 3.0.7 on 2020-07-23 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20200721_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='marcavehiculo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='marcas_logos/%Y/%m/%d', verbose_name='Imagen de marca'),
        ),
    ]
