# Generated by Django 3.2.4 on 2021-11-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0065_alter_profissional_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profissional',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/%Y/%m/'),
        ),
    ]