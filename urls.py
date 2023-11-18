from rest_framework import routers
from app import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tiles', views.TileViewSet, basename='Tiles List')
router.register(r'tasks', views.TaskViewSet, basename='Tasks List')

urlpatterns = [
    path('', include(router.urls)),
]
