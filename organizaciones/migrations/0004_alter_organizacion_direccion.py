# Generated by Django 3.2.6 on 2021-10-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0003_auto_20211029_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='direccion',
            field=models.TextField(help_text='Ejemplo: Maipu 123, Godoy Cruz, Mendoza', max_length=20, null=True),
        ),
    ]