from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'date_joined'
    )
    list_display_links = ('id', 'username')
    search_fields = ('username',)


admin.site.register(User, UserAdmin)
