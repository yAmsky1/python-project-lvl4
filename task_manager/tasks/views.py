from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from ..mixins import CheckPermissionMixin
from task_manager.users.models import User
from .models import Task
from .forms import TaskForm

from ..translations import (
    TASK_LIST_TITLE,
    TASK_CREATED_MESSAGE,
    CREATE_TASK_TITLE,
    CREATE_BUTTON,
    TASK_CHANGED_MESSAGE,
    CHANGE_TASK_TITLE,
    CHANGE_BUTTON,
    TASK_DELETED_MESSAGE,
    NOT_AUTHORIZED_MESSAGE,
    DELETERIGHTS_MESSAGE,
    DELETE_TASK_TITLE,
    DELETE_BUTTON,
)


class TasksList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = TASK_LIST_TITLE
        return context


class CreateTask(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    model = Task
    template_name = 'form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')
    success_message = TASK_CREATED_MESSAGE

    def form_valid(self, form):
        form.instance.created_by = User.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = CREATE_TASK_TITLE
        context['button_text'] = CREATE_BUTTON
        return context


class ChangeTask(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Task
    template_name = 'form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')
    success_message = TASK_CHANGED_MESSAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = CHANGE_TASK_TITLE
        context['button_text'] = CHANGE_BUTTON
        return context


class DeleteTask(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CheckPermissionMixin,
    DeleteView,
):
    model = Task
    template_name = "delete.html"
    success_url = reverse_lazy('tasks:list')
    success_message = TASK_DELETED_MESSAGE
    no_permission_url = 'login'
    error_message = NOT_AUTHORIZED_MESSAGE

    def form_valid(self, form):
        if self.request.user == self.get_object().created_by:
            super().form_valid(form)
        else:
            messages.error(self.request, DELETERIGHTS_MESSAGE)
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = DELETE_TASK_TITLE
        context['button_text'] = DELETE_BUTTON
        return context
