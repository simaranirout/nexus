# Generated by Django 3.2.5 on 2021-07-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instalJob', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jobtime',
            field=models.TimeField(),
        ),
    ]