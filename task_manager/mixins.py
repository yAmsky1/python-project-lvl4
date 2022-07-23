
from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy

NO_PERMISSION_MESSAGE = gettext_lazy('You cannot change other users!')
LOGIN_REQUIRED = gettext_lazy('You are not authorized. Please, log in.')


class CheckPermissionMixin(AccessMixin):
    no_permission_url = 'users:list'

    def handle_no_permission(self):
        messages.error(self.request, NO_PERMISSION_MESSAGE)
        return redirect(self.no_permission_url)


class LoginRequiredMixin(AccessMixin):
    no_auth_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, LOGIN_REQUIRED)
            return redirect(self.no_auth_url)
        return super().dispatch(request, *args, **kwargs)
