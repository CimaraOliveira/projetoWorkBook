# Generated by Django 3.2.4 on 2021-08-30 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('avaliacao', '0011_auto_20210817_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='profissional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profissional', to=settings.AUTH_USER_MODEL),
        ),
    ]
