# Generated by Django 3.2.4 on 2021-07-13 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0020_alter_usuario_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='fotosperfil/%Y/%m/'),
        ),
    ]
