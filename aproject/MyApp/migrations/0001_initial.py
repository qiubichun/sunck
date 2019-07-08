# Generated by Django 2.1.7 on 2019-04-06 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=20, verbose_name='班级名')),
                ('gtime', models.DateTimeField()),
                ('ggnumber', models.IntegerField()),
                ('gnnumber', models.IntegerField()),
                ('gDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '班级表班级表班级表',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(default='', max_length=20, verbose_name='主键')),
                ('sgender', models.BooleanField(default=True)),
                ('sage', models.IntegerField()),
                ('scontent', models.CharField(max_length=40)),
                ('sDelete', models.BooleanField(default=False)),
                ('sgrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sgrade_students', to='MyApp.Grades')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(default='', max_length=20, verbose_name='主键')),
                ('tgender', models.BooleanField(default=True)),
                ('tage', models.IntegerField()),
                ('tcontent', models.CharField(max_length=40)),
                ('tDelete', models.BooleanField(default=False)),
                ('tgrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tgrade_teachers', to='MyApp.Grades')),
            ],
        ),
    ]
