import datetime
from django.db import models


status_options = (('live', 'Live'), ('pending', 'Pending'), ('archived', 'Archived'))
task_types = (('survey', 'Survey'), ('discussion', 'Discussion'), ('diary', 'Diary'))


class Tile(models.Model):
    launch_date = models.DateField(default=datetime.date.today)
    status = models.CharField(choices=status_options, default='pending', max_length=10, unique=False)

    def save(self, *args, **kwargs):
        if self.launch_date == datetime.date.today:
            self.status = 'live'
        super().save(*args, **kwargs)


class Task(models.Model):
    tile = models.ForeignKey(Tile, related_name='tasks', on_delete=models.CASCADE)
    order = models.IntegerField(unique=False)
    type = models.CharField(choices=task_types, max_length=10, unique=False)
    title = models.CharField(max_length=32, default='', unique=False)
    description = models.CharField(max_length=255, default='task_description', unique=False)

    class Meta:
        ordering = ['order']
