# Generated by Django 2.1.1 on 2018-09-20 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0010_auto_20180919_0434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='plataforma',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='twitch',
        ),
    ]