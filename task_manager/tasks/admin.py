from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'status',
        'created_by',
        'executor',
        'created_at',
        'modified_at',
    )
    search_fields = ('name',)


admin.site.register(Task, TaskAdmin)
