# Generated by Django 3.2.6 on 2021-11-01 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donacionV2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cantidad_insumo_donacion',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cantidad_insumo_donacion',
            name='fc',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cantidad_insumo_donacion',
            name='fm',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cantidad_insumo_donacion',
            name='uc',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cantidad_insumo_donacion',
            name='um',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
