# Generated by Django 4.2 on 2023-07-07 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=300000)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2023, 7, 7, 14, 23, 54, 827117, tzinfo=datetime.timezone.utc))),
                ('draft', models.BooleanField(default=True)),
            ],
        ),
    ]
