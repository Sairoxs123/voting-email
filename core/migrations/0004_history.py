# Generated by Django 4.1.7 on 2024-04-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_votes_alter_contestants_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('jssid', models.CharField(max_length=10, verbose_name='JSSID')),
                ('student_name', models.CharField(max_length=50, verbose_name='Name')),
                ('contestant_name', models.CharField(max_length=50, verbose_name='Name of Contestant')),
                ('position', models.CharField(max_length=30, verbose_name='Position')),
            ],
        ),
    ]
