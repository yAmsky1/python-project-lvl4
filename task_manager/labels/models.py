from django.db import models
from ..translations import (
    LABEL_NAME,
    LABEL_CREATED_AT,
    VERBOSE_LABEL_NAME,
    VERBOSE_LABEL_NAME_PL,
)


MAX_LENGTH = 255


class Label(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH,
        null=False,
        verbose_name=LABEL_NAME,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=LABEL_CREATED_AT,
    )
    modified_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name = VERBOSE_LABEL_NAME
        verbose_name_plural = VERBOSE_LABEL_NAME_PL
        ordering = ['id']

    def __str__(self):
        return self.name
