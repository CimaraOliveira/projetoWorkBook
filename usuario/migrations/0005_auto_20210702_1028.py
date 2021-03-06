# Generated by Django 3.2.4 on 2021-07-02 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20210702_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='perfil',
        ),
        migrations.AddField(
            model_name='perfil',
            name='cidade',
            field=models.CharField(default=-1, max_length=250, verbose_name='cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='profissao',
            field=models.CharField(default=-1, max_length=250, verbose_name='Profissao'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario'),
            preserve_default=False,
        ),
    ]
