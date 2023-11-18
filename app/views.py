from rest_framework import viewsets

from app.models import Tile, Task
from app.serializers import TileSerializer, TaskSerializer


class TileViewSet(viewsets.ModelViewSet):
    serializer_class = TileSerializer

    def get_queryset(self):
        queryset = Tile.objects.all().order_by('launch_date').prefetch_related().all()
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status__iexact=status)
        return queryset


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
