import django_filters
from django_filters.filters import ChoiceFilter, BooleanFilter
from django.forms import CheckboxInput
from django.db.models import Value
from django.db.models.functions import Concat

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import User
from .models import Task
from ..translations import (
    EXECUTIVE_LABEL,
    LABEL_LABEL,
    OWN_TASKS_LABEL,
    STATUS_LABEL,
)


class TasksFilter(django_filters.FilterSet):
    all_statuses = Status.objects.values_list('id', 'name', named=True).all()
    status = ChoiceFilter(
        label=STATUS_LABEL,
        choices=all_statuses,
    )
    all_labels = Label.objects.values_list('id', 'name', named=True).all()
    labels = ChoiceFilter(
        label=LABEL_LABEL,
        choices=all_labels,
    )

    all_executors = User.objects.values_list(
        'id',
        Concat('first_name', Value(' '), 'last_name'),
        named=True,
    ).all()
    executor = ChoiceFilter(
        label=EXECUTIVE_LABEL,
        choices=all_executors,
    )

    own_task = BooleanFilter(
        label=OWN_TASKS_LABEL,
        widget=CheckboxInput(),
        method='filter_own_tasks',
        field_name='own_tasks',
    )

    def filter_own_tasks(self, queryset, name, value):
        if value:
            queryset = queryset.filter(created_by=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
