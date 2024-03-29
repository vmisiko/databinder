# Generated by Django 2.2.5 on 2020-08-21 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20200820_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=5),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
