# Generated by Django 3.2.4 on 2021-08-16 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificacoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacao',
            name='lido',
            field=models.BooleanField(default=False),
        ),
    ]
