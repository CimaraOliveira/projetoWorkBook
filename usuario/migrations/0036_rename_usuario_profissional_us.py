# Generated by Django 3.2.4 on 2021-08-18 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0035_profissional_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profissional',
            old_name='usuario',
            new_name='us',
        ),
    ]
