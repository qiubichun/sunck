# Generated by Django 2.1.7 on 2019-05-28 06:56

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grades',
            options={},
        ),
        migrations.AlterModelManagers(
            name='grades',
            managers=[
                ('graobj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='students',
            managers=[
                ('graobj', django.db.models.manager.Manager()),
            ],
        ),
    ]