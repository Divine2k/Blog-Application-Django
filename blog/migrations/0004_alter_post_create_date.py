# Generated by Django 3.2.5 on 2022-06-12 11:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220612_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 11, 5, 53, 784968, tzinfo=utc)),
        ),
    ]