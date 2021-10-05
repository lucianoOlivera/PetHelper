# Generated by Django 3.2.6 on 2021-10-01 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donacion', '0007_auto_20211001_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud_donacion_insumo',
            name='cant_insumo',
        ),
        migrations.AddField(
            model_name='cantidad_insumo',
            name='solicitud_insumo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donacion.solicitud_donacion_insumo'),
        ),
    ]
