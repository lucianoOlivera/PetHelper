# Generated by Django 3.2.6 on 2021-09-27 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donacion', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud_donacion_insumo',
            name='descripcion',
        ),
    ]
