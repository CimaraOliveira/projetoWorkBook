# Generated by Django 3.2.4 on 2021-08-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0005_auto_20210813_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='data',
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='data_avaliacao',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
