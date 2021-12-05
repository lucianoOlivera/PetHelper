# Generated by Django 3.2.6 on 2021-11-17 23:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0005_veterinario_calificacion_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinica',
            name='calificacion',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='clinica',
            name='calificacion_total',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
