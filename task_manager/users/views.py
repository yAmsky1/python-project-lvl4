from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy

from task_manager.mixins import CheckPermissionMixin, LoginRequiredMixin
from .forms import CreateUserForm
from .models import User


# Translations
REGISTER_USER_BUTTON = gettext_lazy('Register')
CHANGE_USER_BUTTON = gettext_lazy('Change')
DELETE_USER_BUTTON = gettext_lazy('Delete')

USER_CREATED_MESSAGE = gettext_lazy('User created successfully!')
USER_CHANGED_MESSAGE = gettext_lazy('User profile changed successfully!')
USER_DELETED_MESSAGE = gettext_lazy('User deleted!')

VERBOSE_NAME = gettext_lazy('User')
VERBOSE_NAME_PL = gettext_lazy('Users')

USER_LIST_TITLE = gettext_lazy('Users')
CREATE_USER_TITLE = gettext_lazy('Create user')
CHANGE_USER_TITLE = gettext_lazy('Change user')
DELETE_USER_TITLE = gettext_lazy('Delete user')


class UsersList(ListView):
    model = User
    template_name = 'users/users.html'
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
        context['button_text'] = CHANGE_USER_BUTTON
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
        context['button_text'] = DELETE_USER_BUTTON
        return context
