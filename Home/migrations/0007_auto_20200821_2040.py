# Generated by Django 2.2.5 on 2020-08-21 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20200821_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='user',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
