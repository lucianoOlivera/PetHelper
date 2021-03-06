# Generated by Django 3.2.6 on 2021-12-12 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud_Donacion_Monetaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('titulo', models.TextField(max_length=100)),
                ('pedido', models.ImageField(blank=True, null=True, upload_to='solicitud')),
                ('monto', models.FloatField(max_length=100)),
                ('cbu', models.PositiveBigIntegerField(blank=True, null=True)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre_titular', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre_banco', models.PositiveSmallIntegerField(choices=[(1, 'Patagonia'), (2, 'Supervielle'), (3, 'ICBC'), (4, 'Banco de la Nación Argentina'), (5, 'Credicoop'), (6, 'Comafi'), (7, 'Santander'), (8, 'HSBC')], default='1')),
                ('EstadoSolicitudMonetaria', models.PositiveSmallIntegerField(default='0')),
                ('uc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('veterinario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organizaciones.veterinario')),
            ],
            options={
                'verbose_name_plural': 'solicitudes_monetarias',
            },
        ),
        migrations.CreateModel(
            name='Solicitud_Donacion_Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('titulo', models.TextField(max_length=100)),
                ('pedido', models.ImageField(blank=True, null=True, upload_to='solicitud')),
                ('EstadoSolicitudInsumo', models.PositiveSmallIntegerField(default='0')),
                ('uc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('veterinario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organizaciones.veterinario')),
            ],
            options={
                'verbose_name_plural': 'solicitudes_insumos',
            },
        ),
        migrations.CreateModel(
            name='Estado_Solicitud_Monetaria_Detalle',
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
                'verbose_name_plural': 'estados_solicitudes_monetarias_detalle',
            },
        ),
        migrations.CreateModel(
            name='Estado_Solicitud_Monetaria',
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
                'verbose_name_plural': 'estados_solicitudes_monetarias',
            },
        ),
        migrations.CreateModel(
            name='Estado_Solicitud_Insumo_Detalle',
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
                'verbose_name_plural': 'estados_solicitudes_monetarias_detalle',
            },
        ),
        migrations.CreateModel(
            name='Estado_Solicitud_Insumo',
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
                'verbose_name_plural': 'estados_solicitudes_insumos',
            },
        ),
    ]
