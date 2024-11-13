from rest_framework import viewsets

from task_manager_tasks.models import Task
from task_manager_tasks.serializers import TaskBaseSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskBaseSerializer
    queryset = Task.objects.all()
