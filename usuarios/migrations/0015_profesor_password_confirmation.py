# Generated by Django 5.1.1 on 2024-10-05 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0014_profesor_alter_usuarios_profile_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='password_confirmation',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
