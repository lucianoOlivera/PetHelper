# Generated by Django 3.2.6 on 2021-11-22 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0003_auto_20211122_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud_donacion_monetaria',
            name='nombre_banco',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Patagonia'), (2, 'Supervielle'), (3, 'ICBC'), (4, 'Banco de la Nación Argentina'), (5, 'Credicoop'), (6, 'Comafi'), (7, 'Santander'), (8, 'HSBC')], default='1'),
        ),
    ]
