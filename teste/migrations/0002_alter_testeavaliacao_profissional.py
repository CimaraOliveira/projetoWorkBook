# Generated by Django 3.2.4 on 2021-08-06 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0025_remove_usuario_status'),
        ('teste', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testeavaliacao',
            name='profissional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarioProfissional', to='usuario.profissional'),
        ),
    ]
