# Generated by Django 3.2.6 on 2021-10-25 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0001_initial'),
        ('insumo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cantidad_insumo',
            name='solicitud_insumo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitud.solicitud_donacion_insumo'),
        ),
    ]
