# Generated by Django 3.2.6 on 2021-10-31 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]