# Generated by Django 3.2.5 on 2021-08-04 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210730_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 6, 13, 14, 37, 260372)),
        ),
    ]
