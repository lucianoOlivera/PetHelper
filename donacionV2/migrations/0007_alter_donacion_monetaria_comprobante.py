# Generated by Django 3.2.6 on 2021-11-22 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donacionV2', '0006_alter_donacion_monetaria_comprobante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion_monetaria',
            name='comprobante',
            field=models.FileField(blank=True, null=True, upload_to='comprobante'),
        ),
    ]