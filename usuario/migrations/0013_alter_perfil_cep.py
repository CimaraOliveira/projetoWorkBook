# Generated by Django 3.2.4 on 2021-07-03 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0012_auto_20210702_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cep',
            field=models.CharField(max_length=10, verbose_name='cep'),
        ),
    ]
