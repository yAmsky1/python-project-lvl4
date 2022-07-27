from django import forms
from .models import Task

from ..translations import (
    TASK_NAME,
    TASK_DESCRIPTION,
    TASK_STATUS,
    TASK_EXECUTIVE,
    TASK_LABEL,
)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'status',
            'executor',
            'labels'
        ]

        label = {
            'name': TASK_NAME,
            'description': TASK_DESCRIPTION,
            'status': TASK_STATUS,
            'executor': TASK_EXECUTIVE,
            'label': TASK_LABEL,
        }
