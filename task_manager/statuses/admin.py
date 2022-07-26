from django.contrib import admin
from .models import Status


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
        'modified_at',
    )
    search_fields = ('name',)


admin.site.register(Status, UserAdmin)
