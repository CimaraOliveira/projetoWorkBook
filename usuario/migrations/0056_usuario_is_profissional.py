# Generated by Django 3.2.4 on 2021-08-26 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0055_auto_20210825_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_profissional',
            field=models.BooleanField(default=False),
        ),
    ]
