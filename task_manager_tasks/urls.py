from django.urls import path, include
from rest_framework import routers

from task_manager_tasks.views import TaskViewSet

router = routers.DefaultRouter()

router.register("tasks", TaskViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "tasks"
