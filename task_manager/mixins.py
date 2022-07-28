from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .translations import (
    NO_PERMISSION_MESSAGE,
    NOT_AUTHORIZED_MESSAGE,
    USER_DELETED_MESSAGE,
    STATUS_DELETED_MESSAGE,
    LABEL_DELETED_MESSAGE,
    ERROR_LABEL_IN_USE_MESSAGE,
    ERROR_STATUS_IN_USE_MESSAGE,
    ERROR_USER_IN_USE_MESSAGE
)


SUCCESS_URLS = {
    'User': reverse_lazy('users:list'),
    'Status': reverse_lazy('statuses:list'),
    'Label': reverse_lazy('labels:list'),
}
SUCCESS_MESSAGES = {
    'User': USER_DELETED_MESSAGE,
    'Status': STATUS_DELETED_MESSAGE,
    'Label': LABEL_DELETED_MESSAGE,
}
ERROR_MESSAGES = {
    'User': ERROR_USER_IN_USE_MESSAGE,
    'Status': ERROR_STATUS_IN_USE_MESSAGE,
    'Label': ERROR_LABEL_IN_USE_MESSAGE,
}


class CheckPermissionMixin(AccessMixin):
    no_permission_url = 'users:list'

    def handle_no_permission(self):
        messages.error(self.request, NO_PERMISSION_MESSAGE)
        return redirect(self.no_permission_url)


class LoginRequiredMixin(AccessMixin):
    no_auth_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, NOT_AUTHORIZED_MESSAGE)
            return redirect(self.no_auth_url)
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin(AccessMixin):

    def form_valid(self, form):
        try:
            model_name = str(self.object.__class__.__name__)
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, ERROR_MESSAGES[model_name])
        else:
            messages.success(self.request, SUCCESS_MESSAGES[model_name])
        return HttpResponseRedirect(SUCCESS_URLS[model_name])
