from rest_framework import serializers

from task_manager_tasks.models import Task


class TaskBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "title", "text", "tags", "owner", "status", "start_date", "dead_line"
        ]
