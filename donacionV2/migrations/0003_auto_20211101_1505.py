# Generated by Django 3.2.6 on 2021-11-01 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donacionV2', '0002_auto_20211101_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cantidad_insumo_donacion',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='cantidad_insumo_donacion',
            name='fm',
        ),
        migrations.RemoveField(
            model_name='cantidad_insumo_donacion',
            name='uc',
        ),
        migrations.RemoveField(
            model_name='cantidad_insumo_donacion',
            name='um',
        ),
    ]
