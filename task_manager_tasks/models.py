from django.contrib.auth import get_user_model
from django.db import models


class Task(models.Model):
    class StatusChoices(models.TextChoices):
        TO_DO = "To do"
        IN_ACTION = "in action"
        DONE = "Done"

    title = models.TextField(max_length=30)
    text = models.CharField(null=True, blank=True)
    status = models.CharField(
        choices=StatusChoices, default=StatusChoices.TO_DO
    )
    tags = models.TextField(max_length=30, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    dead_line = models.DateTimeField(null=True, blank=True)
    owner = models.ManyToManyField(get_user_model(), on_delete=models.CASCADE)
