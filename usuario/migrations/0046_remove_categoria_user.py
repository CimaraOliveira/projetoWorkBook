# Generated by Django 3.2.4 on 2021-08-24 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0045_rename_acesso_profissional_acesso_permitido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='user',
        ),
    ]
