# Generated by Django 3.2.6 on 2021-11-04 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0010_auto_20211102_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinica',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='clinica'),
        ),
        migrations.AlterField(
            model_name='organizacion',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='organizacion'),
        ),
        migrations.AlterField(
            model_name='veterinario',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='veterinario'),
        ),
    ]
