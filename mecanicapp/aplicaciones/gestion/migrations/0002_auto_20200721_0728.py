# Generated by Django 3.0.7 on 2020-07-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasolinera',
            name='descripcion',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='gasolinera',
            name='direccion',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='gasolinera',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre *'),
        ),
        migrations.AlterField(
            model_name='lavadero',
            name='correo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='lavadero',
            name='descripcion',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='lavadero',
            name='direccion',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='lavadero',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre *'),
        ),
        migrations.AlterField(
            model_name='lavadero',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='lavado',
            name='nota',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='nota',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='taller',
            name='correo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='taller',
            name='descripcion',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='taller',
            name='direccion',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='taller',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre *'),
        ),
        migrations.AlterField(
            model_name='taller',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='tipolavado',
            name='descripcion',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='tipolavado',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre *'),
        ),
        migrations.AlterField(
            model_name='tipomantenimiento',
            name='descripcion',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='tipomantenimiento',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre *'),
        ),
    ]
