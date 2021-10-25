# Generated by Django 3.2.6 on 2021-11-30 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_alter_usuario_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='permiso',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Helper'), (2, 'Veterinario'), (3, 'Organizacion'), (4, 'Clinica')], default=1, null=True),
        ),
    ]