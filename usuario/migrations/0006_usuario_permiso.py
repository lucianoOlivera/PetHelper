# Generated by Django 3.2.6 on 2021-11-06 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('usuario', '0005_auto_20211103_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='permiso',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='test1', to='auth.group'),
            preserve_default=False,
        ),
    ]
