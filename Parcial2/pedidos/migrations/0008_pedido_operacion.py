# Generated by Django 4.1.1 on 2022-10-09 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_remove_pedido_active_account_remove_pedido_cui_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='operacion',
            field=models.CharField(default='compra', max_length=50),
        ),
    ]
