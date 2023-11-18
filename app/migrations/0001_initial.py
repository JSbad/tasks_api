# Generated by Django 4.2.7 on 2023-11-16 12:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_date', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(choices=[('live', 'Live'), ('pending', 'Pending'), ('archived', 'Archived')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('type', models.CharField(choices=[('survey', 'Survey'), ('discussion', 'Discussion'), ('diary', 'Diary')], max_length=10)),
                ('title', models.CharField(default='', max_length=32)),
                ('description', models.CharField(default='task_description', max_length=255)),
                ('tile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tile')),
            ],
        ),
    ]