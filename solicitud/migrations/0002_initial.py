# Generated by Django 3.2.6 on 2021-11-21 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('solicitud', '0001_initial'),
        ('organizaciones', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud_donacion_monetaria',
            name='uc',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solicitud_donacion_monetaria',
            name='veterinario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organizaciones.veterinario'),
        ),
        migrations.AddField(
            model_name='solicitud_donacion_insumo',
            name='uc',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solicitud_donacion_insumo',
            name='veterinario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organizaciones.veterinario'),
        ),
        migrations.AddField(
            model_name='estado_solicitud_monetaria_detalle',
            name='uc',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='estado_solicitud_monetaria',
            name='uc',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='estado_solicitud_insumo_detalle',
            name='uc',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='estado_solicitud_insumo',
            name='uc',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
