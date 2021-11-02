# Generated by Django 3.2.6 on 2021-11-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0007_alter_clinica_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='direccion',
            field=models.CharField(help_text='Ejemplo: Maipu 123, Godoy Cruz, Mendoza', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='veterinario',
            name='direccion',
            field=models.CharField(help_text='Ejemplo: Maipu 123, Godoy Cruz, Mendoza', max_length=50, null=True),
        ),
    ]