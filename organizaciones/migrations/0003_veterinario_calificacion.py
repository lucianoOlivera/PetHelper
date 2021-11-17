# Generated by Django 3.2.6 on 2021-11-16 13:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veterinario',
            name='calificacion',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
