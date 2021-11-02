# Generated by Django 3.2.6 on 2021-11-02 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('donacionV2', '0001_initial'),
        ('solicitud', '0001_initial'),
        ('insumo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='donacion_monetaria',
            name='solicitud_monetaria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitud.solicitud_donacion_monetaria'),
        ),
        migrations.AddField(
            model_name='donacion_monetaria',
            name='uc',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='donacion_insumo',
            name='solicitud_insumo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitud.solicitud_donacion_insumo'),
        ),
        migrations.AddField(
            model_name='donacion_insumo',
            name='uc',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cantidad_insumo_donacion',
            name='donacion_isumo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donacionV2.donacion_insumo'),
        ),
        migrations.AddField(
            model_name='cantidad_insumo_donacion',
            name='insumo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insumo.insumo'),
        ),
    ]