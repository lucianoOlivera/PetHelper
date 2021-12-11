# Generated by Django 3.2.6 on 2021-12-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cantidad_Insumo_Donacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('fc', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'cantidad_insumos_donacion',
            },
        ),
        migrations.CreateModel(
            name='Donacion_Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('fechaCreacion', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'donaciones_insumos',
            },
        ),
        migrations.CreateModel(
            name='Donacion_monetaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('monto', models.FloatField(max_length=100)),
                ('comprobante', models.FileField(blank=True, null=True, upload_to='comprobante')),
            ],
            options={
                'verbose_name_plural': 'donaciones_monetaria',
            },
        ),
        migrations.CreateModel(
            name='Estado_Donacion_Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'estados_Donaciones_insumos',
            },
        ),
        migrations.CreateModel(
            name='Estado_Donacion_Insumo_Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'estados_Donaciones_monetarias_detalle',
            },
        ),
        migrations.CreateModel(
            name='Estado_Donacion_Monetaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'estados_Donaciones_monetarias',
            },
        ),
        migrations.CreateModel(
            name='Estado_Donacion_Monetaria_Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'estados_Donaciones_monetarias_detalle',
            },
        ),
        migrations.CreateModel(
            name='Medio_Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombre_pago', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='pagos')),
            ],
            options={
                'verbose_name_plural': 'medios_pagos',
            },
        ),
    ]