# Generated by Django 3.2.6 on 2021-11-07 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('solicitud', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insumo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medio_Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombre_pago', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='pothos')),
                ('uc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'medios_pagos',
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
                ('uc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('uc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'estados_Donaciones_monetarias',
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
                ('uc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'estados_Donaciones_monetarias_detalle',
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
                ('uc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'estados_Donaciones_insumos',
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
                ('solicitud_monetaria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitud.solicitud_donacion_monetaria')),
                ('uc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'donaciones_monetaria',
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
                ('solicitud_insumo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitud.solicitud_donacion_insumo')),
                ('uc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'donaciones_insumos',
            },
        ),
        migrations.CreateModel(
            name='Cantidad_Insumo_Donacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('donacion_isumo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donacionV2.donacion_insumo')),
                ('insumo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insumo.insumo')),
            ],
            options={
                'verbose_name_plural': 'cantidad_insumos_donacion',
            },
        ),
    ]
