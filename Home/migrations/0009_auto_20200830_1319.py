# Generated by Django 2.2.5 on 2020-08-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20200821_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=5),
        ),
    ]