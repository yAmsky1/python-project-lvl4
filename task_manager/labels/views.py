from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView)

from ..mixins import CheckPermissionMixin, FormValidMixin
from .forms import LabelForm
from .models import Label
from ..translations import (
    NOT_AUTHORIZED_MESSAGE,
    LABELS_LIST_TITLE,
    LABEL_CREATED_MESSAGE,
    CREATE_LABEL_TITLE,
    CREATE_BUTTON,
    LABEL_CHANGED_MESSAGE,
    CHANGE_TASK_TITLE,
    CHANGE_BUTTON,
    LABEL_DELETED_MESSAGE,
    DELETE_LABEL_TITLE,
    DELETE_BUTTON,
)


class LabelsList(
    LoginRequiredMixin,
    CheckPermissionMixin,
    ListView,
):

    model = Label
    template_name = "labels/labels_list.html"
    context_object_name = "labels"
    no_permission_url = "login"
    error_message = NOT_AUTHORIZED_MESSAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = LABELS_LIST_TITLE
        return context


class CreateLabel(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CheckPermissionMixin,
    CreateView,
):
    model = Label
    form_class = LabelForm
    template_name = "form.html"
    success_url = reverse_lazy('labels:list')
    success_message = LABEL_CREATED_MESSAGE
    no_permission_url = 'login'
    error_message = NOT_AUTHORIZED_MESSAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = CREATE_LABEL_TITLE
        context['button_text'] = CREATE_BUTTON
        return context


class ChangeLabel(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CheckPermissionMixin,
    UpdateView,
):

    model = Label
    form_class = LabelForm
    template_name = "form.html"
    success_url = reverse_lazy('labels:list')
    success_message = LABEL_CHANGED_MESSAGE
    no_permission_url = 'login'
    error_message = NOT_AUTHORIZED_MESSAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = CHANGE_TASK_TITLE
        context['button_text'] = CHANGE_BUTTON
        return context


class DeleteLabel(
    LoginRequiredMixin,
    FormValidMixin,
    SuccessMessageMixin,
    DeleteView,
):

    model = Label
    template_name = "delete.html"
    success_url = reverse_lazy('labels:list')
    success_message = LABEL_DELETED_MESSAGE
    no_permission_url = 'login'
    error_message = NOT_AUTHORIZED_MESSAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = DELETE_LABEL_TITLE
        context['button_text'] = DELETE_BUTTON
        return context
