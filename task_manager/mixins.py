from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

from .translations import NO_PERMISSION_MESSAGE, LOGIN_REQUIRED_MESSAGE


class CheckPermissionMixin(AccessMixin):
    no_permission_url = 'users:list'

    def handle_no_permission(self):
        messages.error(self.request, NO_PERMISSION_MESSAGE)
        return redirect(self.no_permission_url)


class LoginRequiredMixin(AccessMixin):
    no_auth_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, LOGIN_REQUIRED_MESSAGE)
            return redirect(self.no_auth_url)
        return super().dispatch(request, *args, **kwargs)
