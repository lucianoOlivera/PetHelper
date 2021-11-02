# Generated by Django 3.2.6 on 2021-11-02 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('a', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'insumos',
            },
        ),
        migrations.CreateModel(
            name='Cantidad_Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('insumo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insumo.insumo')),
            ],
            options={
                'verbose_name_plural': 'cantidad_insumos',
            },
        ),
    ]
