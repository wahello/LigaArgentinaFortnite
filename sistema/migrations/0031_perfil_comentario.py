# Generated by Django 2.1.1 on 2018-10-03 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0030_auto_20181003_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='comentario',
            field=models.CharField(blank=True, default=0, max_length=100),
        ),
    ]
