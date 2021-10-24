# Generated by Django 3.2.6 on 2021-10-22 23:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('cuit', models.CharField(default='', max_length=11, unique=True)),
                ('whatsapp', models.CharField(help_text='Ejemplo: 26127483945', max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Debe ingresar un número válido para Argentina', regex='(?:(?:00)?549?)?0?(?:11|[2368]\\d)(?:(?=\\d{0,2}15)\\d{2})??\\d{8}')])),
                ('telefono', models.CharField(default='', help_text='Ejemplo: 2614247398', max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Debe ingresar un número válido para Argentina', regex='(?:(?:00)?549?)?0?(?:11|[2368]\\d)(?:(?=\\d{0,2}15)\\d{2})??\\d{8}')])),
            ],
            options={
                'verbose_name_plural': 'clinicas',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('cuit', models.CharField(default='', max_length=11, unique=True)),
                ('telefono', models.CharField(default='', help_text='Ejemplo: 2614247398', max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Debe ingresar un número válido para Argentina', regex='(?:(?:00)?549?)?0?(?:11|[2368]\\d)(?:(?=\\d{0,2}15)\\d{2})??\\d{8}')])),
            ],
            options={
                'verbose_name_plural': 'organizaciones',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('apellido', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('matricula', models.CharField(default='', max_length=4, unique=True)),
                ('whatsapp', models.CharField(help_text='Ejemplo: 2614247398', max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Debe ingresar un número válido para Argentina', regex='(?:(?:00)?549?)?0?(?:11|[2368]\\d)(?:(?=\\d{0,2}15)\\d{2})??\\d{8}')])),
            ],
            options={
                'verbose_name_plural': 'veterinarios',
            },
        ),
    ]