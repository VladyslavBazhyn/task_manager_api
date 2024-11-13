from django.contrib.auth import get_user_model
from django.db import models


class Task(models.Model):
    class StatusChoices(models.TextChoices):
        TO_DO = "To do"
        IN_ACTION = "In action"
        DONE = "Done"

    title = models.TextField(max_length=30)
    text = models.CharField(null=True, blank=True, max_length=255)
    status = models.CharField(
        choices=StatusChoices, default=StatusChoices.TO_DO, max_length=10
    )
    tags = models.TextField(max_length=30, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    dead_line = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    workers = models.ManyToManyField(get_user_model(), related_name="foreign_tasks")
