from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.mixins import CheckPermissionMixin, LoginRequiredMixin

from .forms import CreateUserForm
from .models import User
from ..translations import (
    REGISTER_USER_BUTTON,
    CHANGE_BUTTON,
    DELETE_BUTTON,
    USER_CREATED_MESSAGE,
    USER_CHANGED_MESSAGE,
    USER_DELETED_MESSAGE,
    USER_LIST_TITLE,
    CREATE_USER_TITLE,
    CHANGE_USER_TITLE,
    DELETE_USER_TITLE,
)


class UsersList(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = USER_LIST_TITLE
        return context


class CreateUser(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'form.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    success_message = USER_CREATED_MESSAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = CREATE_USER_TITLE
        context['button_text'] = REGISTER_USER_BUTTON
        return context


class ChangeUser(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UserPassesTestMixin,
    CheckPermissionMixin,
    UpdateView
):
    model = User
    template_name = 'form.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('users:list')
    success_message = USER_CHANGED_MESSAGE

    def test_func(self):
        return self.request.user == self.get_object()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = CHANGE_USER_TITLE
        context['button_text'] = CHANGE_BUTTON
        return context


class DeleteUser(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    CheckPermissionMixin,
    DeleteView
):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('users:list')
    success_message = USER_DELETED_MESSAGE

    def test_func(self):
        return self.request.user == self.get_object()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = DELETE_USER_TITLE
        context['button_text'] = DELETE_BUTTON
        return context
