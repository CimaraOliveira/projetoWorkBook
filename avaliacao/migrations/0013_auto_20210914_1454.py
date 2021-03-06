# Generated by Django 3.2.4 on 2021-09-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0012_alter_avaliacao_profissional'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='media',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Media'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='soma',
            field=models.IntegerField(blank=True, null=True, verbose_name='Soma'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='total_pessoas',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total Pessoas'),
        ),
    ]
