# Generated by Django 3.2.4 on 2021-07-05 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0014_auto_20210705_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario'),
            preserve_default=False,
        ),
    ]
