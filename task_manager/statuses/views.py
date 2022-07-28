# from django.contrib.auth.mixins import
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from ..mixins import (
    CheckPermissionMixin,
    LoginRequiredMixin,
    FormValidMixin,
)

from .forms import StatusForm
from .models import Status
from ..translations import (
    STATUS_LIST_TITLE,
    STATUS_CREATED_MESSAGE,
    CREATE_STATUS_TITLE,
    CREATE_BUTTON,
    STATUS_CHANGED_MESSAGE,
    CHANGE_STATUS_TITLE,
    CHANGE_BUTTON,
    DELETE_STATUS_TITLE,
    DELETE_BUTTON,
    STATUS_DELETED_MESSAGE,
    NOT_AUTHORIZED_MESSAGE,
)

STATUS_LIST_TEMPLATE = 'statuses/statuses_list.html'
FORM_TEMPLATE = 'form.html'
DELETE_TEMPLATE = 'delete.html'


class StatusesList(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = STATUS_LIST_TITLE
        return context


class CreateStatus(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    model = Status
    template_name = FORM_TEMPLATE
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list')
    success_message = STATUS_CREATED_MESSAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = CREATE_STATUS_TITLE
        context['button_text'] = CREATE_BUTTON
        return context


class ChangeStatus(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list')
    success_message = STATUS_CHANGED_MESSAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = CHANGE_STATUS_TITLE
        context['button_text'] = CHANGE_BUTTON
        return context


class DeleteStatus(
    LoginRequiredMixin,
    FormValidMixin,
    SuccessMessageMixin,
    CheckPermissionMixin,
    DeleteView,
):
    model = Status
    template_name = 'delete.html'
    success_url = reverse_lazy('statuses:list')
    success_message = STATUS_DELETED_MESSAGE
    no_permission_url = 'login'
    error_message = NOT_AUTHORIZED_MESSAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = DELETE_STATUS_TITLE
        context['button_text'] = DELETE_BUTTON
        return context
