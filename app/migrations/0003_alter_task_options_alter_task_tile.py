# Generated by Django 4.2.7 on 2023-11-18 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_tile_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='task',
            name='tile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='app.tile'),
        ),
    ]
