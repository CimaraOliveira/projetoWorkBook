# Generated by Django 3.2.4 on 2021-07-03 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_auto_20210702_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='bairro',
            field=models.CharField(default=1, max_length=40, verbose_name='cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='cep',
            field=models.IntegerField(default=1, max_length=10, verbose_name='cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='uf',
            field=models.CharField(default=1, max_length=2, verbose_name='cidade'),
            preserve_default=False,
        ),
    ]
