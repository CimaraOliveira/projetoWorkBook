# Generated by Django 3.2.4 on 2021-08-16 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0026_alter_profissional_options'),
        ('teste', '0008_alter_testeavaliacao_profissional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testeavaliacao',
            name='profissional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarioProfissional', to='usuario.profissional'),
        ),
    ]