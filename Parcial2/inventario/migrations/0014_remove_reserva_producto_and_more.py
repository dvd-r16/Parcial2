# Generated by Django 5.1.1 on 2024-10-13 03:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0013_reserva_foto_alter_reserva_datos_adicionales_and_more'),
        ('usuarios', '0021_profesor_telefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='producto',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='datos_adicionales',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_bebe/'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.profesor'),
        ),
        migrations.AlterModelTable(
            name='reserva',
            table='reserva_consultas',
        ),
    ]
