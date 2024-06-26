# Generated by Django 4.1.7 on 2024-04-15 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('jssid', models.CharField(max_length=10, verbose_name='JSSID')),
            ],
        ),
        migrations.RemoveField(
            model_name='votes',
            name='jssid',
        ),
        migrations.AddField(
            model_name='history',
            name='date',
            field=models.DateField(default=datetime.date(2024, 4, 15), verbose_name='Date'),
        ),
    ]
