from rest_framework import serializers
from app.models import Tile, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'type', 'description', 'order', 'tile')


class TileSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Tile
        fields = ('id', 'launch_date', 'status', 'tasks')
