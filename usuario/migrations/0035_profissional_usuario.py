# Generated by Django 3.2.4 on 2021-08-18 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0034_alter_profissional_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profissional',
            name='usuario',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='usuario.usuario'),
            preserve_default=False,
        ),
    ]
