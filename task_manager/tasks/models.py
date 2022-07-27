from django.db import models

from task_manager.statuses.models import Status
from task_manager.users.models import User
from ..translations import (
    TASK_NAME,
    TASK_DESCRIPTION,
    TASK_STATUS,
    VERBOSE_TASK_NAME,
    VERBOSE_TASK_NAME_PL,
    TASK_EXECUTIVE,
)


MAX_LENGTH = 255


class Task(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name=TASK_NAME)
    description = models.TextField(null=False, verbose_name=TASK_DESCRIPTION)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
        verbose_name=TASK_STATUS,
        related_name='task')
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=False,
        related_name='task',
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        related_name="works",
        verbose_name=TASK_EXECUTIVE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name = VERBOSE_TASK_NAME
        verbose_name_plural = VERBOSE_TASK_NAME_PL
        ordering = ['id']

    def __str__(self):
        return self.name
