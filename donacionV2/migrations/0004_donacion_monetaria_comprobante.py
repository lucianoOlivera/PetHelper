# Generated by Django 3.2.6 on 2021-11-22 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donacionV2', '0003_alter_medio_pago_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='donacion_monetaria',
            name='comprobante',
            field=models.ImageField(blank=True, null=True, upload_to='comprobante'),
        ),
    ]
