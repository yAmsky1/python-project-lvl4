from django.db import models
from ..translations import (
    VERBOSE_STATUS_NAME,
    VERBOSE_STATUS_NAME_PL,
    STATUS_CREATED_AT,
    STATUS_NAME,
)


MAX_LENGTH = 255


class Status(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH,
        null=False,
        verbose_name=STATUS_NAME)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=STATUS_CREATED_AT
    )
    modified_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = VERBOSE_STATUS_NAME
        verbose_name_plural = VERBOSE_STATUS_NAME_PL
        ordering = ['id']
