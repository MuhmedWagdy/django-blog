# Generated by Django 4.2 on 2023-07-09 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 9, 12, 16, 34, 450706, tzinfo=datetime.timezone.utc)),
        ),
    ]