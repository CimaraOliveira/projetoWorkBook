# Generated by Django 3.2.4 on 2021-09-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0061_remove_profissional_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='profissional',
            name='cpf',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
