# Generated by Django 2.1.1 on 2018-11-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0034_auto_20181109_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='black_pan',
            field=models.CharField(blank=True, default='NO', max_length=100),
        ),
    ]