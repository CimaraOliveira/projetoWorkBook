# Generated by Django 3.2.4 on 2021-08-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0006_alter_testeavaliacao_profissional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testeavaliacao',
            name='descricao',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='descricao'),
        ),
    ]