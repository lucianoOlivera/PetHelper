# Generated by Django 3.2.6 on 2021-11-06 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('usuario', '0006_usuario_permiso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='permiso',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='test1', to='auth.group'),
        ),
    ]
